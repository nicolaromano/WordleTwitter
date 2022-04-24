import twint
import pandas as pd
import numpy as np
from tqdm import tqdm
import os


def scrapeTwitter(keyword: str, limit: int = 100, csv_output: str = "tweets.csv") -> None:
    """
    Scrape twitter for tweets containing a keyword.

    Parameters:
        keyword (str): The keyword to search for.
        limit (int): The number of tweets to scrape. Default is 100. Pass None for no limit.
        csv_output (str): The path to the csv file to output to. Defaults to "tweets.csv".

    Returns:
        None
    """

    # Delete the csv file if it exists
    if os.path.isfile(csv_output):
        os.remove(csv_output)

    c = twint.Config()

    c.Search = keyword
    if limit is not None:
        c.Limit = limit
    c.Output = csv_output
    c.Store_csv = True
    c.Hide_output = True

    twint.run.Search(c)

filename = "WordleTweets.csv"
scrapeTwitter("#wordle", limit=None, csv_output=filename)