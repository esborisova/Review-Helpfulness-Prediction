"""Pipeline for training binary review helpfulness classifiers based on votes up values."""

import sys

sys.path.append("../helpfulness_prediction")
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from scipy import sparse
from scipy.sparse import hstack
from sklearn.preprocessing import OneHotEncoder
from preprocess import identity_tokenizer


df = pd.read_pickle("../../data/data_with_features.pkl")
df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(0, inplace=True)

features = df.drop(
    [
        "steamid",
        "review",
        "votes_up",
        "votes_funny",
        "timestamp_created",
        "weighted_vote_score",
        "comment_count",
        "cleaned",
        "tokenized",
        "vu_label",
        "wvs_label",
        "partially_cleaned",
    ],
    axis=1,
)

labels = df["vu_label"].reset_index(drop=True)

# In the original dataset the numb of help and unhelp reviews in train, test sets was balanced
# Might need a solution for an imbalanced case
x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.20)

tfidf_vectorizer = TfidfVectorizer(
    lowercase=False, tokenizer=identity_tokenizer, ngram_range=(1, 2), min_df=0.02
)
X_train = tfidf_vectorizer.fit_transform(x_train["lemmatized"])
X_test = tfidf_vectorizer.transform(x_test["lemmatized"])
print(X_train.shape, X_test.shape)

voted_up_train = x_train["voted_up"].to_list()
voted_up_test = x_test["voted_up"].to_list()

enc = OneHotEncoder()
voted_up_train = enc.fit_transform(voted_up_train).toarray()
voted_up_test = enc.fit_transform(voted_up_test).toarray()

vader_train = x_train[["vader_pos", "vader_neg", "vader_neu"]].to_numpy()
vader_test = x_test[["vader_pos", "vader_neg", "vader_neu"]].to_numpy()

x_train = x_train.drop(
    ["lemmatized", "voted_up", "vader_pos", "vader_neg", "vader_neu"], axis=1
)
x_test = x_test.drop(
    ["lemmatized", "voted_up", "vader_pos", "vader_neg", "vader_neu"], axis=1
)

x_train_np = np.array(x_train)
x_test_np = np.array(x_test)

x_train_sp = sparse.csr_matrix(x_train_np)
x_test_sp = sparse.csr_matrix(x_test_np)
print(x_train_sp.shape, x_test_sp.shape)

voted_up_train_sp = sparse.csr_matrix(voted_up_train)
voted_up_test_sp = sparse.csr_matrix(voted_up_test)

vader_train_sp = sparse.csr_matrix(vader_train)
vader_test_sp = sparse.csr_matrix(vader_test)

X_train_stacked = hstack([X_train, x_train_sp, voted_up_train_sp, vader_train_sp])
X_test_stacked = hstack([X_test, x_test_sp, voted_up_test_sp, vader_test_sp])
print(X_train_stacked.shape, X_test_stacked.shape)

X_train_arr = X_train_stacked.toarray()
X_test_arr = X_test_stacked.toarray()

scaler = StandardScaler()
X_scalled_train = scaler.fit_transform(X_train_arr)
X_scalled_test = scaler.fit_transform(X_test_arr)

LR = LogisticRegression()
LR.fit(X_scalled_train, y_train)
y_pred_re = LR.predict(X_scalled_test)

LR_report = classification_report(y_test, y_pred_re)
print(LR_report)

RF = RandomForestClassifier(n_estimators=100, random_state=15325)
RF.fit(X_scalled_train, y_train)
y_pred_rf = RF.predict(X_scalled_test)

RF_report = classification_report(y_test, y_pred_rf)
print(RF_report)
