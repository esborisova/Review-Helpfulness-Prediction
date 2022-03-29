import urllib.request 
import urllib.parse 
import json
import pandas as pd
from typing import List


# Not used functions

#def check_duplicates(data: List[dict]) -> List[int]:
#    """Checks for duplicate reviews
#
#    Args:
#        data (List[dict]): A list with dictionaries containing reviews
#    
#    Returns:
#        List[int]: A list with indexes of duplicate reviews 
#    
#    """
#    index_to_remove = []
#    size = len(data)
#    uniqueNames = []
#    
#    for i in range(size):  
#        if(data[i]["author"]["steamid"] not in uniqueNames):
#            uniqueNames.append(data[i]["author"]["steamid"]) 
#        else:  
#            index_to_remove.append(i)
#    
#    return index_to_remove



#def remove_duplicates(data: List[dict], 
#                      indexes: List[int]) -> List[dict]:
#    """Removes duplicate reviews
#
#    Args:
#        data (List[dict]): A list with dictionaries containing reviews
#        indexes (List[int]): A list of indexes for duplicates
#    
#    Returns:
#        List[dic]: A list of dictionaries (json format) containing reviews without duplicates
#    
#    """
#    step = 0
#    
#    for i in indexes:
#        if (step == 0):
#            del data[i]
#            step +=1
#        elif (step > 0):
#            del data[i-step]
#            step +=1
#
#    return data



def update_url(base_url: str,
               id_to_add: List[str],
               split_char: str,
               id_to_replace_index: int):

    splitted_url = base_url.split(split_char) 
    url_part1_size = len(splitted_url[0])
    id_removed = splitted_url[0][:url_part1_size - id_to_replace_index]

    new_url = id_removed + id_to_add + '?' + splitted_url[1]

    return new_url



def collect_reviews(url_base: str, 
                    num_pages: int, 
                    review_key: str,
                    cursor_key: str) -> List[dict]:
    """Collects reviews per page from Steam via API

    Args:
        url_base (str): A string containg url with a game id 
        num_pages (int): The number of pages to loop over and save reviews
        review_key (str): A key for reviews
        cursor_key (str): A key for a cursor
    
    Returns:
        List[dict]: A list of dictionaries (json format) containing all review/reviewer info
    
    """

    next_cursor = '*'
    data = []

    for i in range(num_pages):
        url_temp = url_base + next_cursor
        url = urllib.request.urlopen(url_temp)
        tmp_data = json.loads(url.read().decode())
        for i in range(len(tmp_data[review_key])):
            data.append(tmp_data[review_key][i])
            next_cursor = urllib.parse.quote(tmp_data[cursor_key]) 
  
    return data



def json_to_df(data: List[dict]) -> pd.DataFrame:
    """Creates a dataframe from json formated reviews

    Args:
        data (List[dict]): A list with dictionaries containing reviews
    
    Returns:
        pd.DataFrame: A dataframe with reviews
    
    """

    df = pd.DataFrame(columns=['steamid', 
                               'num_games_owned', 
                               'num_reviews', 
                               'playtime_forever', 
                               'review', 
                               'timestamp_created', 
                               'voted_up', 
                               'votes_up', 
                               'votes_funny',
                               'weighted_vote_score', 
                               'comment_count'])


    for review in data:
        steamid = review['author']['steamid']
        num_games_owned = review['author']['num_games_owned']
        num_reviews = review['author']['num_reviews']
        playtime = review['author']['playtime_forever']
        text = review['review']
        timestamp = review['timestamp_created']
        voted_up  = review['voted_up']
        votes_up = review['votes_up']
        votes_funny = review['votes_funny']
        wvs = review['weighted_vote_score']
        comment_count = review['comment_count']


        row = [steamid, 
               num_games_owned, 
               num_reviews,
               playtime,
               text,
               timestamp,
               voted_up,
               votes_up,
               votes_funny,
               wvs,
               comment_count]

        
        df.loc[len(df)] = row
    
    
    return df





url_base = 'https://store.steampowered.com/appreviews/374320?json=1&filter=recent&num_per_page=100&cursor='
ids = ['374320','275850', '377160', '218620', '221100', '319630', '227300', '346110', '264710', '242760', '107410', '578080', '435150', '814380', '431960', '322330', '239140', '250900', '289070', '261550', '252490', '413150', '271590', '582010', '620', '550']

#'1174180'- json decoder error (Red Dead Redumption)

data = []
for id in ids:
    print(id)
    if id not in url_base:
        url_base = update_url(base_url = url_base,
                              id_to_add = id,
                              split_char = '?',
                              id_to_replace_index = len(id))
                  
    data.append(collect_reviews(url_base = url_base, 
                                num_pages = 2,
                                review_key = 'reviews',
                                cursor_key = 'cursor'))

flat_list = [item for sublist in data for item in sublist]

df = json_to_df(flat_list)
df = df.drop_duplicates(subset=['steamid'], keep = 'first')