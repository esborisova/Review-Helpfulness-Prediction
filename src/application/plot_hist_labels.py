"""Script for plotting reviews distribution across Y values."""

import sys

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_pickle("../../data/with_labels.pkl")

fig, ax = plt.subplots()
df[str(sys.argv[1])].hist(bins=30, figsize=(10, 7), ax=ax)
fig.savefig(f"../../figs/{str(sys.argv[1])}_hist.pdf")
