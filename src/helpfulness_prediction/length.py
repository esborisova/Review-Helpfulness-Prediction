import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")


def count_sents(text: str) -> int:
    """
    Counts the number of sentences in a string.

    Args:
        text (str): A string with sentences.

    Returns:
        int: The number of sentences.
    """
    sents = nltk.sent_tokenize(text)
    return len(sents)


def count_pars(text: str) -> int:
    """
    Counts the number of paragraphs in a string.

    Args:
        text (str): A string to count paragraphs in.

    Returns:
        int: The number of paragraphs.
    """
    pars = text.split("\n")
    pars = [par for par in pars if par != ""]
    return len(pars)
