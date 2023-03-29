"""
testing processing functions

There are very few aspects to test here, simply that the data is maintained
throughout.
"""
from datetime import datetime
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
    scenarios. Parameterized test cases are pulled from above and each is run
    through this checking function.
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
        (read_to_variable(NAME), "2021-12-12", 3),
        # check when range extends into different month
        (read_to_variable(NAME), "2020-02-01", 6),
        # check for when range extends into different year
        (read_to_variable(NAME), "2018-12-29", 9),
    ],
)
def test_get_tweets_around(tweet_list, mid_date, ssearch_range):
    """
    test
    """
    pass
