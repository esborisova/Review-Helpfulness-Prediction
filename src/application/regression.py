"""Pipeline for training regression models for review helpfulness prediction based on weighted vote score."""

import sys

sys.path.append("../helpfulness_prediction")
import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from scipy.sparse import hstack
from scipy import sparse
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

labels = df["wvs_label"].reset_index(drop=True)

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.20)

tfidf_vectorizer = TfidfVectorizer(
    lowercase=False, tokenizer=identity_tokenizer, ngram_range=(1, 2), min_df=0.02
)
X_train = tfidf_vectorizer.fit_transform(x_train["lemmatized"])
X_test = tfidf_vectorizer.transform(x_test["lemmatized"])

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

RF = RandomForestRegressor(max_depth=2, random_state=0, n_estimators=100)
RF.fit(X_scalled_train, y_train)
y_pred_rf = RF.predict(X_scalled_test)
y_pred_train_rf = RF.predict(X_scalled_train)

mae_rf = metrics.mean_absolute_error(y_test, y_pred_rf)
mse_rf = metrics.mean_squared_error(y_test, y_pred_rf)
rmse_rf = np.sqrt(metrics.mean_squared_error(y_test, y_pred_rf))
r2_test_rf = metrics.r2_score(y_test, y_pred_rf)
r2_train_rf = metrics.r2_score(y_train, y_pred_train_rf)

rf_regressor = {
    "MAE": mae_rf,
    "MSE": mse_rf,
    "RMSE": rmse_rf,
    "R2_test": r2_test_rf,
    "R2_train": r2_train_rf,
}

RR = Ridge()
RR.fit(X_scalled_train, y_train)
y_pred_lr = RR.predict(X_scalled_test)
y_pred_train_lr = RR.predict(X_scalled_train)

mae_lr = metrics.mean_absolute_error(y_test, y_pred_lr)
mse_lr = metrics.mean_squared_error(y_test, y_pred_lr)
rmse_lr = np.sqrt(metrics.mean_squared_error(y_test, y_pred_lr))
r2_test_lr = metrics.r2_score(y_test, y_pred_lr)
r2_train_lr = metrics.r2_score(y_train, y_pred_train_lr)

linear_regressor = {
    "MAE": mae_lr,
    "MSE": mse_lr,
    "RMSE": rmse_lr,
    "R2_test": r2_test_lr,
    "R2_train": r2_train_lr,
}

scores = pd.DataFrame(rf_regressor, index=["RF"])
scores.loc["LR"] = linear_regressor

scores.to_pickle("../../data/pkl/regression_scores.pkl")
