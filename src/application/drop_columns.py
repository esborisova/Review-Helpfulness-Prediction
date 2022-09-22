"""Script for removing irrelavant columns from df for correlation analysis."""

import pandas as pd

df = pd.read_pickle("../../data/data_with_features.pkl")

features_labels = df.drop(
    [
        "steamid",
        "timestamp_created",
        "review",
        "votes_funny",
        "comment_count",
        "cleaned",
        "tokenized",
        "lemmatized",
        "partially_cleaned",
    ],
    axis=1,
)

features_labels.to_pickle("../../data/df_features_labels.pkl")
