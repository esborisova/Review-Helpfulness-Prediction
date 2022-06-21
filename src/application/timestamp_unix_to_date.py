"""Script for transforming review date creation from unix to year, month, day format."""

import pandas as pd
from datetime import datetime


df = pd.read_pickle("../../data/with_gramm_cat.pkl")

df["year"] = 0
df["month"] = 0
df["day"] = 0

for row in range(len(df)):
    df["year"].iloc[row] = datetime.utcfromtimestamp(
        df["timestamp_created"].iloc[row]
    ).strftime("%Y")
    df["month"].iloc[row] = datetime.utcfromtimestamp(
        df["timestamp_created"].iloc[row]
    ).strftime("%m")
    df["day"].iloc[row] = datetime.utcfromtimestamp(
        df["timestamp_created"].iloc[row]
    ).strftime("%d")

df.to_pickle("../../data/data_with_features.pkl")
