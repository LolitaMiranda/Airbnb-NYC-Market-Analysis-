"""Visualization functions for the Airbnb NYC project."""

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def _save_figure(output_path: str | Path | None) -> None:
    if output_path:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        plt.savefig(output_path, dpi=300, bbox_inches="tight")


def plot_price_by_room_type(
    df: pd.DataFrame, output_path: str | Path | None = None
) -> None:
    plt.figure(figsize=(9, 5))
    sns.barplot(data=df, x="room_type", y="price", errorbar=None)
    plt.title("Average Listing Price by Room Type")
    plt.xlabel("Room Type")
    plt.ylabel("Average Price (USD)")
    plt.tight_layout()
    _save_figure(output_path)
    plt.show()


def plot_reviews_by_borough(
    df: pd.DataFrame, output_path: str | Path | None = None
) -> None:
    totals = (
        df.groupby("neighbourhood_group", as_index=False)["number_of_reviews"]
        .sum()
        .sort_values("number_of_reviews", ascending=False)
    )
    plt.figure(figsize=(9, 5))
    sns.barplot(data=totals, x="neighbourhood_group", y="number_of_reviews")
    plt.title("Total Reviews by Borough")
    plt.xlabel("Borough")
    plt.ylabel("Total Reviews")
    plt.tight_layout()
    _save_figure(output_path)
    plt.show()


def plot_listing_map(
    df: pd.DataFrame, output_path: str | Path | None = None
) -> None:
    plt.figure(figsize=(8, 8))
    plt.scatter(df["longitude"], df["latitude"], s=3, alpha=0.35)
    plt.title("Geographic Distribution of Airbnb Listings")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()
    _save_figure(output_path)
    plt.show()
