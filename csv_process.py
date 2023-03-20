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
    # read the raw data in based on name and year
    with open(f"raw-data/{name}-after-{year}.csv", "r") as f:

        # sets reader object
        reader = csv.reader(f)
        # generates empty row list
        rows = []
        # appends every row in the csv to new list
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
        # pulls the string with the date values
        temp_date = tweet[0]
        # converts the string to a date time object
        dt_obj = datetime.strptime(temp_date, "%Y-%m-%d %H:%M:%S%z")
        # pulls the date and converts it to standard format
        tweet_date = dt_obj.strftime("%m-%d-%Y")
        # appends the tweet data if it matches the target date
        if tweet_date == date:
            specific_tweets.append(tweet)
    return specific_tweets


def write_to_csv(data, filename):
    """
    Writes the new data to a csv in the processed-data folder.

    Args:
        data (list): a list of data to write to a csv.
        filename (str): the name of the csv to store the data in.

    Returns:
        None.
    """
    # opens a new csv with the specified filename
    with open(f"processed-data/{filename}.csv", mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        # iterate through the list and append data to csv on separate rows
        for row in data:
            csv_writer.writerow(row)
