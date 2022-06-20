"""Pipeline for collecting FRI, ARI and GFI readability scores per review."""

import pandas as pd
import textstat

df = pd.read_pickle("../../data/with_polarity.pkl")

df["FRE"] = df["cleaned"].apply(textstat.flesch_reading_ease)
df["ARI"] = df["cleaned"].apply(textstat.automated_readability_index)
df["GFI"] = df["cleaned"].apply(textstat.gunning_fog)

df.to_pickle("../../data/with_readability.pkl")
