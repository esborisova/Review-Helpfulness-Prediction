import sys

sys.path.append("../src/helpfulness_prediction")
import spacy
from preprocess import collect_tokens


def test_tokenizer():
    nlp = spacy.load("en_core_web_lg")
    test_sent = "the dot product may be defined algebraically or geometrically"

    tokens = collect_tokens(test_sent, nlp=nlp)

    assert tokens == [
        "the",
        "dot",
        "product",
        "may",
        "be",
        "defined",
        "algebraically",
        "or",
        "geometrically",
    ]

    for token in tokens:
        assert isinstance(token, str)
