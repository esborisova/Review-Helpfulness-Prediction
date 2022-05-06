import sys

sys.path.append("../src/helpfulness_prediction")
from preprocess import rm_single_char


def test_single_ch():

    test_tokens = ["party", "tomorrow", "s", ""]
    tokens = rm_single_char(test_tokens)

    assert tokens == ["party", "tomorrow"]

    for token in tokens:
        assert isinstance(token, str)
