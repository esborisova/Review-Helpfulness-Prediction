import pandas as pd
from sklearn import preprocessing 
from sklearn.preprocessing import OneHotEncoder 


df = pd.read_pickle("../../data/with_gramm_cat.pkl")
enc = preprocessing.OneHotEncoder()

voted_up = df["voted_up"].tolist()

encoding = enc.fit(voted_up)
sentiment_voted_up = encoding.transform(voted_up).toarray()