import pandas as pd
from typing import Tuple


def assign_class_label(
    df: pd.DataFrame, y_column: str, label_column: str, threshold: Tuple[int, float]
) -> pd.DataFrame:
    """Returns 0 or 1 based on the threshold.

    Args:
        df (pd.DataFrame): A pandas dataframe with data.
        y_column (str): The dataframe column containg Y values.
        label_column (str): The dataframe column to save the results.
        threshold (Tuple[int, float]): The cut off based on which 0 or 1 are assigned.
        If a given value is larger than the given threshold, 1 is returned, otherwise 0.

    Returns:
        pd.DataFrame: A dataframe with 0 or 1 values per Y.
    """
    for row in range(len(df)):
        if df[y_column].iloc[row] > threshold:
            df[label_column].iloc[row] = 1
    return df
