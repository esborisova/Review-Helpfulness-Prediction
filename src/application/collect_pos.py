"""Pipeline for counting the percentage of nouns, verbs, adjectives per review."""

import pandas as pd
import spacy
import sys

sys.path.append("../helpfulness_prediction")
from preprocess import clean
from gramm_categories import count_pos


nlp = spacy.load("en_core_web_lg")
df = pd.read_pickle("../../data/with_length.pkl")

df["NN"] = 0
df["VB"] = 0
df["JJ"] = 0

tags_nn = ["NN", "NNS", "NNP", "NNPS"]
tags_vb = ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]
tags_adj = ["JJ", "JJR", "JJS"]

for row in range(len(df)):
    cleaned_rev = clean(df["review"].iloc[row])

    df["NN"].iloc[row] = count_pos(cleaned_rev, nlp, tags_nn) / df["N_words"].iloc[row]
    df["VB"].iloc[row] = count_pos(cleaned_rev, nlp, tags_vb) / df["N_words"].iloc[row]
    df["JJ"].iloc[row] = count_pos(cleaned_rev, nlp, tags_adj) / df["N_words"].iloc[row]

df.to_pickle("../../data/with_gramm_cat.pkl")
