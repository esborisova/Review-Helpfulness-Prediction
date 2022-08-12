import numpy as np
from typing import List
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict 
import logging


class MeanEmbeddingVectorizer():
    """
	Computes average word vectors.

    Typical usage example:
       MEV = MeanEmbeddingVectorizer(model)
       X = MEV.transform(docs)

    Args:
        w2v: Word2vec model.

    Attributes:
        vector_size: Dimensionality of the word vectors.
    """

    def __init__(self, w2v):
        self.w2v = w2v
        self.vector_size = w2v.wv.vector_size

    def fit(self):
        return self

    def transform(self, docs):
        doc_word_vector = self.word_average_list(docs)
        return doc_word_vector

    def word_average(self, sent: List[str]) -> List[np.ndarray]:
        """
        Computes average word vector per doc.

        Args:
            sent (List[str]): A list of tokens/lemmas.

        Returns:
            List[np.ndarray]: A list of averaging word vectors.
        """

        mean = []

        for word in sent:
            if word in self.w2v.wv.index_to_key:
                mean.append(self.w2v.wv.get_vector(word))

        if not mean:
            return np.zeros(self.vector_size)

        else:
            mean = np.array(mean).mean(axis=0)
            return mean

    def word_average_list(self, docs: List[List[str]]) -> List[np.ndarray]:
        """
        Computes average word vector for multiple docs.

        Args:
            docs (List[List[str]]): A list of tokenized/lemmatized docs.

        Returns:
            List[np.ndarray]: An array of average word vector in shape (len(docs),)
        """

        return np.vstack([self.word_average(sent) for sent in docs])


class TfidfEmbeddingVectorizer():
	"""Computes TF-IDF weighed average word vectors.

    Typical usage example:
       TEV = TfidfEmbeddingVectorizer(model)
       X = TEV.transform(docs)

    Args:
        word_model: Word2vec model.
		word_idf_weight: A word idf weight.

    Attributes:
        vector_size: Dimensionality of the word vectors.
    """

	def __init__(self, word_model):

		self.word_model = word_model
		self.word_idf_weight = None
		self.vector_size = word_model.wv.vector_size

	def fit(self, docs: List[List[str]]):  

		text_docs = []

		for doc in docs:
			text_docs.append(" ".join(doc))

		tfidf = TfidfVectorizer()
		tfidf.fit(text_docs)  

		max_idf = max(tfidf.idf_)  
		self.word_idf_weight = defaultdict(lambda: max_idf,
						   [(word, tfidf.idf_[i]) for word, i in tfidf.vocabulary_.items()])
		return self


	def transform(self, docs):  
		doc_word_vector = self.word_average_list(docs)
		return doc_word_vector


	def word_average(self, docs: List[List[str]])-> List[np.ndarray]:
		"""
        Computes tfidf weighted word vector for multiple docs.

        Args:
            docs (List[List[str]]): A list of tokenized/lemmatized docs.

        Returns:
            List[np.ndarray]: An array of average word vector in shape (len(docs),)
        """

		mean = []

		for word in docs:
			if word in self.word_model.wv.vocab:
				mean.append(self.word_model.wv.get_vector(word) * self.word_idf_weight[word]) 

		if not mean: 
			logging.warning("cannot compute average owing to no vector for {}".format(docs))
			return np.zeros(self.vector_size)
		else:
			mean = np.array(mean).mean(axis=0)
			return mean


	def word_average_list(self, docs: List[List[str]]) -> List[np.ndarray]:
		"""
        Computes average word vector for multiple docs.

        Args:
            docs (List[List[str]]): A list of tokenized/lemmatized docs.

        Returns:
            List[np.ndarray]: An array of average word vector in shape (len(docs),)
        """
		return np.vstack([self.word_average(sent) for sent in docs])
