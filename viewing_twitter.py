"""
Testing snscrape library.
"""
# MAY NOT WORK AS FUNCTIONS HAVE BEEN RENAMED - CHECK NOTEBOOK FOR CURRENT
# PROCESS.
import pandas as pd
from basescrape import get_thou_tweets

NAME = input("Enter the name of the profile you want to scrape.\n")
print(f"Scraping {NAME}'s profile for the last 1000 tweets...")
tweets = get_thou_tweets(NAME)
tweet_df = pd.DataFrame(
    tweets, columns=["date", "time", "content", "interaction count"]
)
tweet_df.to_csv(f"data/{NAME}.csv", index=False)
print(f"Done! File saved under data/{NAME}.csv")
