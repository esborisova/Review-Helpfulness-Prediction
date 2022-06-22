"""Pipeline for preprocessing reviews (cleaning, tokenizing, lemmatizing)"""

import pandas as pd
import re
import spacy
import sys

sys.path.append("../helpfulness_prediction")
from preprocess import clean, collect_tokens, collect_lemmas, rm_stops, rm_single_char

nlp = spacy.load("en_core_web_lg")

stops = open("../stop_words.txt", "r")
stops = stops.read().split()

df = pd.read_pickle("../../data/dataset.pkl")

df = df.loc[df["votes_up"] != 0]

df["cleaned"] = ""
df["tokenized"] = ""
df["lemmatized"] = ""

reviews = df["review"].tolist()
cleaned_reviews = [clean(review) for review in reviews]

df["cleaned"] = cleaned_reviews
df = df.loc[df["cleaned"] != ""]

cleaned_rev = df["cleaned"].tolist()

tokenized_reviews = [collect_tokens(review, nlp=nlp) for review in cleaned_rev]
no_stops_tokens = [rm_stops(review, stops) for review in tokenized_reviews]
no_stops_tokens = [rm_single_char(review) for review in no_stops_tokens]

lemmatized_reviews = [collect_lemmas(review, nlp=nlp) for review in cleaned_rev]
no_stops_lemmas = [rm_stops(review, stops) for review in lemmatized_reviews]
no_stops_lemmas = [rm_single_char(review) for review in no_stops_lemmas]


df["tokenized"] = no_stops_tokens
df["lemmatized"] = no_stops_lemmas

df.to_pickle("../../data/preprocessed_data.pkl")
