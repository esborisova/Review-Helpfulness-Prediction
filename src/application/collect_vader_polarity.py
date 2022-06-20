import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

df = pd.read_pickle("../../data/with_labels.pkl")

df["vader_pos"] = 0
df["vader_neg"] = 0
df["vader_neu"] = 0

analyser = SentimentIntensityAnalyzer()

for row in range(len(df)):
    polarity = analyser.polarity_scores(df["cleaned"].iloc[row])
    df["vader_pos"].iloc[row] = polarity["pos"]
    df["vader_neg"].iloc[row] = polarity["neg"]
    df["vader_neu"].iloc[row] = polarity["neu"]

df.to_pickle("../../data/with_polarity.pkl")
