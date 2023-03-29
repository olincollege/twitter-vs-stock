# twitter-vs-stock
Exploring the correlation between tweets of CEOs and their stock value. The full process can be followed in main.ipynb

## Setup

### Repo requirements
To get started, fork this repo.

To access all the elements and visuals in our explanation, you will need to install some prerequisites first. These can be found in the `requirements.txt` file at the root of this repository.


| Library     | Description                   |
| ----------- | ------------------------------|
| snscrape    | Used for tweet scraping       |
| pandas      | Used for creating data frames |
| scikit_learn| Used for statistical analysis |
| yfinance    | Used for scraping stock prices|
| pmdarima    | Used for training SARIMA model|
| matplotlib  | Used for data visualization   |

 To install them, you can run the following at the head of this repo:

```pip install -r requirements.txt```

or

```pip install matplotlib pandas scikit_learn snscrape yfinance pmdarima```

Once these are installed, open the computational essay `main.ipynb` and follow through with the exploration. You should not change any of the code cells unless there is a note stating that they are tester functions designed to build understanding. Running all the code cells is imperative for the variables to be loaded correctly.

All of the visuals will be correct if these steps are followed, and the computational essay provides an in-depth explanation of how we arrive at each stage. 

## Summary
### snscrape Introduction
This program explores how the tweets made by Elon Musk affect the stocks of his largest company, Tesla. After covering reasons why this exploration is useful and defining a research question, we outline our methodology. `snscrape` is used to scrape all the tweets on his profile and store the data in a csv in the raw data folder. Since snscrape's python documentation is undocumented from the library [source](https://github.com/JustAnotherArchivist/snscrape), an overview of the key aspects used to scrape the tweets is included in the methodology.

### Scraping and manipulating stock market data
With the data in the raw folder, the tweet list can now be manipulated based on the stock data. The `yfinance`, `pandas` and `matplotlib` libraries are used to plot the stock prices of Tesla compared to other key indices. This allows us to determine points where the behavior of Tesla's stock is very different compared to the rest of the market. Using the percentage variance (generated with `scikit_learn`) between Tesla stock prices and these other key tech indices, we were able to generate a list of key dates where the Tesla stock price decreased at a disproportionate rate compared to the market.

### Training and implementing SARIMA model for an event study
Using `pmdarima` we then trained and implemented a SARIMA (Seasonal Autoregressive Integrated Moving Average) model in an event study. This allowed us to plot the projected stock graphs for Tesla if the tweet event did not take place, using historic closing data. This would tell us if the tweet event was significant enough to cause a stock drop and verify our hypothesis. For our chosen date we also examined the tweet activity of Elon Musk to confirm that he tweeted something significant on our key date.
Analyzing 5 key stock price drops with tweet content
We then took the 5 key dates with the highest percentage variance and conducted mini-case studies using our tweet processing functions. We analyzed the content of the tweets that were tweeted around the event of the stock price drop and made insights as to whether we thought they were significant enough to be a key factor in the price drop at this time.

### Concluding and evaluating
With all of our results, we then conclude how accurate our hypothesis was. We also evaluate our exploration, looking at ways we could have made it more accurate, and outlining our potential next steps.
