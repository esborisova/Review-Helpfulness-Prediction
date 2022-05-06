"Fucntions for cleaning, tokenizing and lemmatizing reviews"

import pandas as pd
import re
import spacy
from typing import List

nlp = spacy.load("en_core_web_lg")


def clean(text: str) -> str:
    """
    Cleans text from punctuation, double spaces, URLs, special characters and lowercases.

    Args:
        text (str): A string to clean.

    Returns:
        str: A cleaned string.
    """

    no_urls = re.sub(r"http\S+", "", text)
    no_special_ch = re.sub(
        r"(#[A-Za-z]+)|(@[A-Za-z]+)|([^A-Za-z \t])|(\w+:\/\/\S+)", " ", no_urls
    )
    no_special_ch = no_special_ch.replace("\n", " ")
    lowercased = no_special_ch.lower()
    cleaned_text = re.sub(" +", " ", lowercased)
    cleaned_text = cleaned_text.strip()

    return cleaned_text


def rm_stops(text: List[str], stopwords: List[str]) -> List[str]:
    """
    Removes stopwords from tokenized/lemmatized text.

    Args:
        text (List[str]): A list with tokens/lemmas.
        stopwords (List[str]): A list of stopwords.

    Returns:
       List[str]: A list with tokens/lemmas without stopwords.
    """

    no_stopwords = []

    for word in text:
        if word not in stopwords:
            no_stopwords.append(word)

    return no_stopwords


def rm_single_char(text: List[str]) -> List[str]:
    """
    Removes tokens/lemmas which contain less than 2 characters.

    Args:
        text (List[str]): Tokens/lemmas.

    Returns:
        List[str] :A list with tokens/lemmas the length of which is at least 2.
    """
    tokens = []
    for token in text:
        if len(token) >= 2:
            tokens.append(token)
    return tokens


def collect_tokens(text: str) -> List[str]:
    """
    Tokenizes text using spaCy pipeline.

    Args:
        text (str): A string with text to be tokenized.

    Returns:
        List[str]: A list with tokens.
    """

    tokens = []
    doc = nlp(text)
    for token in doc:
        tokens.append(token.text)

    return tokens


def collect_lemmas(text: str) -> List[str]:
    """
    Lemmatizes text using spaCy pipeline.

    Args:
        text (str): A string to be lemmatized.

    Returns:
        List[str]: A list with lemmas.
    """

    lemmas = []
    doc = nlp(text)
    for token in doc:
        lemmas.append(token.lemma_)

    return lemmas
