"""Reusable data-cleaning utilities for the Airbnb NYC project."""

from pathlib import Path
import pandas as pd


def load_data(path: str | Path) -> pd.DataFrame:
    """Load a CSV file and return a DataFrame."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path)


def clean_airbnb_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the Airbnb NYC dataset without discarding valid no-review listings."""
    cleaned = df.copy()

    cleaned = cleaned.drop_duplicates()

    if "reviews_per_month" in cleaned.columns:
        cleaned["reviews_per_month"] = cleaned["reviews_per_month"].fillna(0)

    if "host_name" in cleaned.columns:
        cleaned["host_name"] = cleaned["host_name"].fillna("Unknown")

    if "name" in cleaned.columns:
        cleaned["name"] = cleaned["name"].fillna("Unnamed listing")

    # Keep last_review as datetime; missing values remain NaT for listings with no reviews.
    if "last_review" in cleaned.columns:
        cleaned["last_review"] = pd.to_datetime(
            cleaned["last_review"], errors="coerce"
        )

    numeric_columns = [
        "price", "minimum_nights", "number_of_reviews",
        "reviews_per_month", "calculated_host_listings_count",
        "availability_365", "latitude", "longitude"
    ]
    for column in numeric_columns:
        if column in cleaned.columns:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    cleaned = cleaned.dropna(subset=[
        c for c in ["price", "room_type", "neighbourhood_group"]
        if c in cleaned.columns
    ])

    return cleaned


def save_data(df: pd.DataFrame, path: str | Path) -> None:
    """Save a DataFrame to CSV, creating parent folders when necessary."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
