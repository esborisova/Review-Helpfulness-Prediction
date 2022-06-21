"""Pipeline for plotting Pearson/Spearman correlation coefficients matrix."""

import sys

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


features_labels = pd.read_pickle("../../data/df_features_labels.pkl")

corr_df = features_labels.corr(method=str(sys.argv[1]))
matrix = np.triu(corr_df)

with sns.axes_style("white"):
    fig, ax = plt.subplots(figsize=(20, 25))

sns.set(font_scale=1.2)
sns.heatmap(
    corr_df,
    annot=True,
    linewidth=0.3,
    square=True,
    cmap="coolwarm",
    robust=True,
    ax=ax,
    mask=matrix,
    fmt=".2f",
    cbar_kws={"shrink": 0.9, "orientation": "horizontal"},
)
plt.xticks(fontsize=19, rotation=45, ha="right", rotation_mode="anchor")
plt.yticks(fontsize=19, rotation=0)
plt.savefig(f"../../figs/{str(sys.argv[1])}.pdf")
