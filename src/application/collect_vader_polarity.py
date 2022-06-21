"""Pipeline for preparing reviews for vader sentiment analysis and for collecting polarity scores."""

import sys

sys.path.append("../helpfulness_prediction")
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from preprocess import rm_html

df = pd.read_pickle("../../data/with_labels.pkl")

df["partially_cleaned"] = df["review"].apply(rm_html)

df["vader_pos"] = 0
df["vader_neg"] = 0
df["vader_neu"] = 0

analyser = SentimentIntensityAnalyzer()

for row in range(len(df)):
    polarity = analyser.polarity_scores(df["partially_cleaned"].iloc[row])
    df["vader_pos"].iloc[row] = polarity["pos"]
    df["vader_neg"].iloc[row] = polarity["neg"]
    df["vader_neu"].iloc[row] = polarity["neu"]

df.to_pickle("../../data/with_polarity.pkl")
