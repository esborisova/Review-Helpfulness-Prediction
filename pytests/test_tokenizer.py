import sys

sys.path.append("../src/helpfulness_prediction")
from preprocess import collect_tokens


def test_tokenizer():

    test_sent = "the dot product may be defined algebraically or geometrically"

    tokens = collect_tokens(test_sent)

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
