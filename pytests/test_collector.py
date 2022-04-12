from posixpath import split
import sys

sys.path.append("../helpfulness_prediction")
from collect import update_url


def test_url_change():
    url = "https://store/676?json"
    id = "374320"  #'550', '6475', '2', '53637282293']

    assert (
        update_url(
            url=url, id=id, search_pattern=r"\/\d+\?", sub_pattern="[^A-Za-z0-9]+"
        )
        == "https://store/374320?json"
    )
