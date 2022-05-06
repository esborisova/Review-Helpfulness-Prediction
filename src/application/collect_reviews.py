"""Pipleine for collecting reviews."""

import urllib.request
import urllib.parse
import json
import pandas as pd
from typing import List
import sys

sys.path.append("../helpfulness_prediction")
from collect import update_url, collect_reviews, json_to_df


url_base = "https://store.steampowered.com/appreviews/374320?json=1&filter=recent&num_per_page=100&cursor="
ids = [
    "374320",
    "275850",
    "377160",
    "218620",
    "221100",
    "319630",
    "227300",
    "346110",
    "264710",
    "242760",
    "107410",
    "578080",
    "435150",
    "814380",
    "431960",
    "322330",
    "239140",
    "250900",
    "289070",
    "261550",
    "252490",
    "413150",
    "271590",
    "582010",
    "620",
    "550",
]

#'1174180'- json decoder error (Red Dead Redumption)

data = []

for id in ids:
    if id not in url_base:
        url_base = update_url(
            url=url_base, id=id, search_pattern=r"\/\d+\?", sub_pattern="[^A-Za-z0-9]+"
        )

    data.append(
        collect_reviews(
            url_base=url_base, num_pages=2, review_key="reviews", cursor_key="cursor"
        )
    )

flat_list = [item for sublist in data for item in sublist]

df = json_to_df(flat_list)
df = df.drop_duplicates(subset=["steamid"], keep="first")

df.to_pickle('../../data/dataset.pkl')
