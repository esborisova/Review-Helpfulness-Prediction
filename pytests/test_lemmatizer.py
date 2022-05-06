import sys

sys.path.append("../src/helpfulness_prediction")
from preprocess import collect_lemmas


def test_lemmatizer():

    test_sent = "She has two dogs and a cat"

    tokens = collect_lemmas(test_sent)

    assert tokens == [
        "she",
        "have",
        "two",
        "dog",
        "and",
        "a",
        "cat",
    ]

    for token in tokens:
        assert isinstance(token, str)
