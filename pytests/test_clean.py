import sys

sys.path.append("../src/helpfulness_prediction")
from preprocess import clean


def test_clean_func():

    sent = "Here you can find the   definiton for the dot   product https://en.wikipedia.org/wiki/Dot_product 1111"

    cleaned_sent = clean(sent)

    assert isinstance(cleaned_sent, str)
    assert cleaned_sent == "here you can find the definiton for the dot product"
