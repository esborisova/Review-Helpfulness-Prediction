"Fucntions for cleaning, tokenizing and lemmatizing reviews"

import re
from typing import List


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


def rm_html(text: str) -> str:
    """
    Cleans text from URLs.

    Args:
        text (str): A string to clean.

    Returns:
        str: A cleaned string.
    """

    no_urls = re.sub(r"http\S+", "", text)
    no_special_ch = " ".join(no_urls.split())

    return no_special_ch


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


def collect_tokens(text: str, nlp) -> List[str]:
    """
    Tokenizes text using spaCy pipeline.

    Args:
        text (str): A string with text to be tokenized.
        nlp: A spaCy pipeline.

    Returns:
        List[str]: A list with tokens.
    """

    tokens = []
    doc = nlp(text)
    for token in doc:
        tokens.append(token.text)

    return tokens


def collect_lemmas(text: str, nlp) -> List[str]:
    """
    Lemmatizes text using spaCy pipeline.

    Args:
        text (str): A string to be lemmatized.
        nlp: A spaCy pipeline.

    Returns:
        List[str]: A list with lemmas.
    """

    lemmas = []
    doc = nlp(text)
    for token in doc:
        lemmas.append(token.lemma_)

    return lemmas


def identity_tokenizer(text):
    return text
