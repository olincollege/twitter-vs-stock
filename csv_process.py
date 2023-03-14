"""
Functions for manipulating scraped tweets.
"""
import pandas as pd
import csv
from datetime import datetime


def read_to_variable(name, year):
    """
    Writes all the data in a csv to a variable.

    Args:
        name (str): the name of the user's data to write to csv.
        year (int): the corresponding start year of the tweets in the csv.

    Returns:
        rows (list): list of all tweets with data in the given csv.
    """
    with open(f"raw-data/{name}-after-{year}.csv", "r") as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)

    return rows


def show_tweets_on(tweets, date):
    """
    Takes a list of tweet and returns tweets on a specific day.

    Args:
        tweets (list): list of tweets to sweep through.
        date (str): date of tweets to look for.

    Returns:
        specific_tweets (list): list of all tweets on specified date.

    Note:
        Date must be in the format mm-dd-yyyy.
    """
    specific_tweets = []
    # loop through tweets in list
    for tweet in tweets[1:]:
        temp_date = tweet[0]
        dt_obj = datetime.strptime(temp_date, "%Y-%m-%d %H:%M:%S%z")
        tweet_date = dt_obj.strftime("%m-%d-%Y")
        if tweet_date == date:
            specific_tweets.append(tweet)
    return specific_tweets
