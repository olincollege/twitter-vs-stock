"""
Functions for manipulating scraped tweets.
"""
from datetime import timedelta, datetime
import csv
import pandas as pd


def read_to_variable(name, year=2019):
    """
    Writes all the data in a csv to a variable.

    Args:
        name (str): the name of the user's data to write to csv.
        year (int): the corresponding start year of the tweets in the csv.

    Returns:
        rows (list): list of all tweets with data in the given csv.
    """
    # read the raw data in based on name and year
    with open(
        f"raw-data/{name}-after-{year}.csv", "r", encoding="utf-8"
    ) as file:
        # sets reader object
        reader = csv.reader(file)
        # generates empty row list
        rows = []
        # appends every row in the csv to new list
        for row in reader:
            rows.append(row)

    return rows


def show_tweets_on(tweets, date):
    """
    Takes a list of tweets and returns tweets on a specific day.

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


def get_tweets_around(name, mid_date, search_range=15):
    """
    Finds all the tweets within a specific number of days of an initial date.

    Args:
        name (str): name of profile to grab tweets from.
        mid_date (str): midpoint date to center search around.
        range (int): number of days before and after to search through.

    Returns:
        specific tweets (list): List of all tweets within specified days of
        specified date.

    Note:
        Date must be in format mm-dd-yyyy.
        The default range is set to 15 days.
        This function omits replies.
    """

    # define empty tweets list
    specific_tweets = []

    # convert input date to datetime object
    mid_date = datetime.strptime(mid_date, "%m-%d-%Y")

    # grab tweets based on name input:
    raw_list = read_to_variable(name)

    # create timedelta with input range
    time_delta = timedelta(days=search_range)

    # loop through tweets in list
    for tweet in raw_list[1:]:
        # pulls the string with the date values
        temp_date = tweet[0]

        # pulls tweet content to allow reply omission.
        content = tweet[1]

        # converts the string to a date time object
        tweet_date = datetime.strptime(temp_date, "%Y-%m-%d %H:%M:%S%z")

        # remove the timezone offset
        tweet_date = tweet_date.replace(tzinfo=None)

        # appends the tweet data if within date range and not a reply.
        if (mid_date - time_delta) < tweet_date < (
            mid_date + time_delta
        ) and content[0] not in "@":
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

    # checks if there is data for view count and adjusts column names of data
    # frame.

    tweet = data[0]

    val = tweet[2]

    tweets_df = pd.DataFrame(
        data, columns=["date and time", "content", "view count"]
    )

    if val == "":
        tweets_df = tweets_df.loc[:, tweets_df.columns != "view count"]

    # add dataframe to csv
    tweets_df.to_csv(f"processed-data/{filename}.csv", index=False)
    return tweets_df
