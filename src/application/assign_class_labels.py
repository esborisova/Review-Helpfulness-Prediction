"""Pipeline for labeling Y values with 0 and 1 for binary classification."""

import sys

sys.path.append("../helpfulness_prediction")
import pandas as pd
from set_labels import assign_class_label


df = pd.read_pickle("../../data/preprocessed_data.pkl")

df["weighted_vote_score"] = pd.to_numeric(df["weighted_vote_score"], errors="coerce")
df["weighted_vote_score"].median()

df["vu_label"] = 0
df["wvs_label"] = 0

df = assign_class_label(df, "votes_up", "vu_label", 9)
df = assign_class_label(df, "weighted_vote_score", "wvs_label", 0.5222930312156677)

df.to_pickle("../../data/with_labels.pkl")
