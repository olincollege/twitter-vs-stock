from twitscrape import *
from csv_process import *

NAME = "elonmusk"
YEAR = 2019
DATE = "2022-06-10"
tweets = read_to_variable(NAME, YEAR)
specific_tweets = show_tweets_on(tweets, DATE)
