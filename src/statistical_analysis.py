"""Statistical tests used in the Airbnb NYC project."""

from dataclasses import dataclass
import pandas as pd
from scipy.stats import f_oneway, ttest_ind


@dataclass
class TestResult:
    statistic: float
    p_value: float


def room_type_anova(df: pd.DataFrame) -> TestResult:
    """Test whether average prices differ across room types."""
    groups = [
        group["price"].dropna().values
        for _, group in df.groupby("room_type")
        if len(group["price"].dropna()) > 1
    ]
    if len(groups) < 2:
        raise ValueError("At least two room-type groups are required.")
    statistic, p_value = f_oneway(*groups)
    return TestResult(float(statistic), float(p_value))


def borough_price_ttest(
    df: pd.DataFrame,
    borough_a: str = "Brooklyn",
    borough_b: str = "Manhattan",
) -> TestResult:
    """Compare mean prices between two boroughs using Welch's t-test."""
    sample_a = df.loc[
        df["neighbourhood_group"] == borough_a, "price"
    ].dropna()
    sample_b = df.loc[
        df["neighbourhood_group"] == borough_b, "price"
    ].dropna()

    if sample_a.empty or sample_b.empty:
        raise ValueError("Both borough samples must contain observations.")

    statistic, p_value = ttest_ind(
        sample_a, sample_b, equal_var=False
    )
    return TestResult(float(statistic), float(p_value))
