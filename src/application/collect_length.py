"""Pipeline for collecting review length on character, word, sentence and paragraph level
as well as calculating an average sentence length"""

import sys

sys.path.append("../helpfulness_prediction")
import pandas as pd
from length import count_sents, count_pars


df = pd.read_pickle("../../data/with_readability.pkl")

df["N_words"] = df["tokenized"].apply(lambda x: len(x))
df["N_char"] = df["partially_cleaned"].apply(lambda x: len(x))
df["N_sent"] = df["partially_cleaned"].apply(count_sents)
df["N_par"] = df["review"].apply(count_pars)
df["averg_sent_len"] = 0

for row in range(len(df)):
    df["averg_sent_len"].iloc[row] = df["N_words"].iloc[row]/df["N_sent"].iloc[row]

df.to_pickle("../../data/with_length.pkl")

