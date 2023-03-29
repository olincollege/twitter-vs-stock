"""
tests for twitscrape functions.

Because of the nature of this api, testing for status codes is difficult. These
tests are designed to make sure that all the data is formatted how it is
supposed to be. The functions that grab thousands of tweets have no test cases
as they normally take multiple minutes to run and use the same calls as the
starter functions tested below.
"""
# import twitscrape tests
import datetime
from twitscrape import get_tweet, get_tweet_data

# using the twitter handle of the ex-CEO to test
NAME = "jack"


def test_get_tweet_format():
    """
    Unit test for content of tweet function.

    No arguments or returns. This function checks if the rawContent of the
    tweet is a string or not. This ensures that the scraper pulled the correct
    element.
    """
    # test that content type is a string.
    assert isinstance(get_tweet(NAME), str)


def test_get_tweet_data():
    """
    Unit test for list of data function.

    This function checks if the output list of data is in the correct format,
    and that every element has a value. This again ensures that the data is
    being parsed correctly.

    """
    # define elements of tweet data
    latest_tweet_data = get_tweet_data(NAME)
    sublist = latest_tweet_data[0]
    date = sublist[0]
    content = sublist[1]
    likes = sublist[2]
    retweets = sublist[3]

    # check if there is only 1 sublist inside tweet data list
    assert len(latest_tweet_data) == 1
    # check if the function returns a list containing a sublist of the tweet
    # data
    assert isinstance(latest_tweet_data, list)
    # check if the date is a datetime object
    assert isinstance(date, datetime.datetime)
    # check if the content is a string
    assert isinstance(content, str)
    # check if the likes value is an integer
    assert isinstance(likes, int)
    # check if the retweets value is an integer.
    assert isinstance(retweets, int)
