"""
testing processing functions

There are very few aspects to test here, simply that the data is maintained
throughout.
"""
from datetime import datetime, timedelta
import pytest
from csv_process import read_to_variable, show_tweets_on, get_tweets_around

# all tests will be based on elon musk's processed data
NAME = "elonmusk"


@pytest.mark.parametrize(
    "tweets, dates",
    [
        # test date with same month and day
        (read_to_variable(NAME), "12-12-2021"),
        # test year with duplicate characters
        (read_to_variable(NAME), "01-01-2020"),
        # test older dates (scraper functionality)
        (read_to_variable(NAME), "12-31-2017"),
        (read_to_variable(NAME), "06-13-2014"),
    ],
)
def test_show_tweets_on(tweets, dates):
    """
    Tests if tweets only from the collect date are stored.

    This case using python parameterization to test multiple different date
    scenarios. For each case, the input date is compared against the date of
    every tweet in the list. They need to match for the test to pass.

    Args:
        tweets (list): list of tweets to search through.
        dates (str): date of tweets to search for.
    """


    specific_tweets = show_tweets_on(tweets, dates)
    input_date_obj = datetime.strptime(dates, "%m-%d-%Y")
    for tweet in specific_tweets:
        date_element = tweet[0]
        date = date_element[0:10]
        tweet_date_obj = datetime.strptime(date, "%Y-%m-%d")
        assert tweet_date_obj == input_date_obj


@pytest.mark.parametrize(
    "tweet_list, mid_date, search_range",
    [
        # check when day and month are the same
        (read_to_variable(NAME), "2021-12-12", 3),
        # check when range extends into different month
        (read_to_variable(NAME), "2020-02-01", 6),
        # check for when range extends into different year
        (read_to_variable(NAME), "2018-12-29", 9),
    ],
)
def test_get_tweets_around(tweet_list, mid_date, search_range):
    """
    Tests if all the tweets lie in the correct date range

    This case uses python parameterization to test multiple date scenarios.
    The function calculates the fartheest forward possible date in the date
    range, and the furthest away possible date range in the past, and asserts
    if each tweet in the list lies in the date overall search range.

    Args:
        tweet_list (list): list of tweets to search through.
        mid_date (str): date to search around.
        search_range (int): number of days to search around the mid_date.
    """

    # define tweet list
    tweets_around_list = get_tweets_around(tweet_list, mid_date, search_range)

    # convert input date to datetime object
    input_date_obj = datetime.strptime(mid_date, "%Y-%m-%d")

    # create date range with input date and range
    time_delta = timedelta(days=search_range)
    max_future_date = time_delta + input_date_obj
    max_past_date = input_date_obj - time_delta

    # loop through each tweet in the list and check if in date range
    for tweet in tweets_around_list:
        date_element = tweet[0]
        date = date_element[0:10]
        tweet_date_obj = datetime.strptime(date, "%Y-%m-%d")

        assert max_past_date <= tweet_date_obj <= max_future_date
