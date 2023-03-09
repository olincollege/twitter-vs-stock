from basescrape import *

NAME = "elonmusk"

tweets_df = get_tweets_in_month(NAME, "Feb")
# tested to see attributes generated in "tweet" object.
