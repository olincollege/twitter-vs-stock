"""
Functions testing snscrape functionality
"""

# import twitter scraping library
import pandas as pd
import snscrape.modules.twitter as sntwitter

# import pandas for data processing later


def get_tweet(twitter_handle):
    """
    Gets the most recent tweet from a user.

    Args:
        twitter_handle (str) : Handle of the account to grab tweets from.

    Returns:
        tweet (str) : List of all tweets. and the metadata surrounding them.

    """
    scraper = sntwitter.TwitterUserScraper(twitter_handle).get_items()

    for tweet in scraper:
        content = tweet.rawContent
        break

    return content


def get_tweet_data(twitter_handle):
    """
    Gets the date, time, content, and interaction data for a tweet.

    Args:
        twitter_handle (str) : Handle of the account to grab tweets from.

    Returns:
        tweet_data (list) : List of tweet data.
    """
    scraper = sntwitter.TwitterUserScraper(twitter_handle).get_items()
    tweet_data = []

    for tweet in scraper:
        # create a variable for total interactions (likes + retweets)
        interactions = tweet.likeCount + tweet.retweetCount
        # data being pulled
        data = [tweet.date, tweet.rawContent, interactions]
        # append data from each tweet.
        tweet_data.append(data)
        break

    return tweet_data


def get_tweet_date(twitter_handle):
    """
    Gets the date and time of the most recent tweet as raw output.

    Args:
        twitter_handle (str) : Handle of the account to grab tweets from.

    Returns:
        date (datetime object) : The date and time of the most recent tweet.
    """
    # stores all items of tweet
    scraper = sntwitter.TwitterUserScraper(twitter_handle).get_items()

    # collect the date from the most recent tweet.
    for tweet in scraper:
        date = tweet.date
        break
    return date


def get_thou_tweets(twitter_handle):
    """
    Gets the last 10000 tweets of a user.

    Args:
        twitter_handle (str) : Handle of the account to grab tweets from.

    Returns:
        tweets_df (pd.dataframe) : Pandas dataframe containing data about past
        10000 tweets.

    Note:
    The dates and times are converted to strings for easier comparison, it may
    be necersary to convert them back to datetime objects forplotting.
    """

    tweets_list = []

    # scrape a specific user
    scraper = sntwitter.TwitterUserScraper(twitter_handle).get_items()

    # loop through items in completed scrape
    for i, tweet in enumerate(scraper):
        if i > 10000:
            break
        # splits the date object into date and time elements
        dates = tweet.date
        date = dates.strftime("%b-%d-%Y")
        time = dates.strftime("%H:%m")
        # data being pulled
        data = [date, time, tweet.rawContent, tweet.viewCount]
        # append data from each tweet if in feb.
        tweets_list.append(data)
    # turn data into dataframe (pandas)
    tweets_df = pd.DataFrame(
        tweets_list, columns=["date", "time", "content", "view count"]
    )
    # add dataframe to csv
    tweets_df.to_csv(f"raw-data/{twitter_handle}.csv", index=False)
    return tweets_df


def get_tweets_in_month(twitter_handle, targ_month):
    """
    Scrapes through ALL tweets and returns tweets in specified month.
    Args:
        twitter_handle (str) : Handle of the account to grab tweets from.
        month (str) : First three digits of intended month.

    Returns:
        tweets_df (pd.dataframe) : Pandas dataframe containing data about tweets
        tweeted in given month.
    Note:
    The dates and times are converted to strings for easier comparison, it may
    be necersary to convert them back to datetime objects forplotting. Object
    within object needs to be called on line 148.
    """

    tweets_list = []

    # scrape specified user
    scraper = sntwitter.TwitterUserScraper(twitter_handle).get_items()
    # loop through items in completed scrape
    for i, tweet in enumerate(scraper):
        # splits the date object into date and time elements
        date = tweet.date.strftime("%b-%d-%Y")
        month = date[0:3]
        # get total number of tweets
        user_attributes = tweet.user
        total_tweets = user_attributes.statusesCount
        # break out of loops if loop index passes users total tweet count
        if i > total_tweets:
            break
        # skip to next index if month doesnt match user input
        if month not in targ_month:
            continue
        # data being stored
        data = [tweet.date, tweet.rawContent, tweet.viewCount]
        # append data from each tweet if in specified month
        tweets_list.append(data)
    # turn list into pandas dataframe
    tweets_df = pd.DataFrame(
        tweets_list, columns=["date and time", "content", "view count"]
    )
    # add dataframe to csv
    tweets_df.to_csv(f"month-data/{twitter_handle}.csv", index=False)
    return tweets_df


def get_tweets_before(twitter_handle, before_hour):
    """
    Scrapes through ALL tweets and returns tweets tweeted within specific times.

    Args:
        twitter_handle (str) : Handle of the account to grab tweets from.
        before_hour (int) : specified hour to truncate tweets after
        (24hr format).

    Returns:
        tweets_df (pd.dataframe) : Pandas dataframe containing data about tweets
        tweeted before a specific hour.
    Note:
    The dates and times are converted to strings for easier comparison, it may
    be necersary to convert them back to datetime objects for plotting.
    """

    tweets_list = []

    # scrape specified user
    scraper = sntwitter.TwitterUserScraper(twitter_handle).get_items()
    # loop through items in completed scrape
    for i, tweet in enumerate(scraper):
        # splits the date object into date and time elements
        time = tweet.date.strftime("%H:%m")
        hour = time[0:2]
        # get total number of tweets
        user_attributes = tweet.user
        total_tweets = user_attributes.statusesCount
        # break out of loops if loop index passes users total tweet count
        if i > total_tweets:
            break
        # skip to next index if hour is after cutoff hour
        if hour > before_hour:
            continue
        # data being stored
        data = [tweet.date, tweet.rawContent, tweet.viewCount]
        # append data from each tweet if in specified month
        tweets_list.append(data)
    # turn list into pandas dataframe
    tweets_df = pd.DataFrame(
        tweets_list, columns=["date and time", "content", "view count"]
    )
    # add dataframe to csv
    tweets_df.to_csv(f"month-data/{twitter_handle}.csv", index=False)
    return tweets_df


def get_all_tweets(twitter_handle):
    """
    Scrapes through ALL tweets.

    Args:
        twitter_handle (str) : Handle of the account to grab tweets from.

    Returns:
        tweets_df (pd.dataframe) : Pandas dataframe containing all tweets from
        specified user.
    """

    tweets_list = []

    # scrape specified user
    scraper = sntwitter.TwitterUserScraper(twitter_handle).get_items()
    # loop through items in completed scrape
    for i, tweet in enumerate(scraper):
        # get total number of tweets
        user_attributes = tweet.user
        total_tweets = user_attributes.statusesCount
        # break out of loops if loop index passes users total tweet count
        if i > total_tweets:
            break
        # skip to next index if hour is after cutoff hour
        # data being stored
        data = [tweet.date, tweet.rawContent, tweet.viewCount]
        # append data from each tweet if in specified month
        tweets_list.append(data)
    # turn list into pandas dataframe
    tweets_df = pd.DataFrame(
        tweets_list, columns=["date and time", "content", "view count"]
    )
    # add dataframe to csv
    tweets_df.to_csv(f"month-data/{twitter_handle}.csv", index=False)
    return tweets_df


def get_tweets_after(twitter_handle, year):
    """
    Scrapes through ALL tweets.

    Args:
        twitter_handle (str) : Handle of the account to grab tweets from.
        year (int) : Year of which to print all tweets after.

    Returns:
        tweets_df (pd.dataframe) : Pandas dataframe containing data about tweets
        tweeted after the given year.
    """

    tweets_list = []

    # scrape specified user
    scraper = sntwitter.TwitterUserScraper(twitter_handle).get_items()
    # loop through items in completed scrape
    for tweet in scraper:
        # get current year
        current_year = tweet.date.strftime("%Y")
        # break out of loop when target year is reached
        if current_year == year:
            break
        # data being stored
        data = [tweet.date, tweet.rawContent, tweet.viewCount]
        # append data from each tweet if in specified month
        tweets_list.append(data)
    # turn list into pandas dataframe
    tweets_df = pd.DataFrame(
        tweets_list, columns=["date and time", "content", "view count"]
    )
    # add dataframe to csv
    tweets_df.to_csv(f"raw-data/{twitter_handle}-after-{year}.csv", index=False)
    return tweets_df
