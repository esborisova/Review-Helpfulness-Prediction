import sys

sys.path.append("../src/helpfulness_prediction")
from preprocess import rm_stops


def test_rm_stops():

    stops = open("../src/stop_words.txt", "r")
    stops = stops.read().split()

    test_tokens = ["he", "and", "i", "will", "be", "at", "your", "party", "tomorrow"]
    stops_rm = rm_stops(test_tokens, stops)

    assert stops_rm == ["party", "tomorrow"]

    for token in stops_rm:
        assert isinstance(token, str)
