"""Helper functions for getting and plotting stocks
using the Yfinance library"""

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yahooFinance


def make_stock_dict(ticker_symbols):
    """Autogenerates a dictionary of ticker
    symbols as keys with empty values

    Args:
        ticker_symbols: A list of all the ticker symbols
        we want to use in our graphing.

    Returns:
        a dictionary of ticker symbols as keys and
        empty values"""

    # Create empty dict
    ticker_dict = {}
    for symbol in ticker_symbols:
        ticker_dict[symbol] = None

    return ticker_dict


def get_close_stocks(ticker, start_date, end_date, normalize=False):
    """
    Get's a list of stock close values
     during a specific period of time.

     Args:
        ticker: A dictionary with all the different
        stock symbols as keys
        start_date: A string in the format of YYYY-MM-DD
        which represents the beginning date to get the
        stock prices.
        end_date: A string in the format of YYYY-MM-DD which
        represents the end date to get the stock prices
        normalize: A boolean optional parameter which tells
        the function that the stock data should be normalized.

    Return:
        Return a dictionary with the stock symbols as keys
        and the stock close data beginning from start_date to
        end_date as values"""

    # We go through each stock listed in the ticker and grab the
    # stock data for that stock.
    for symbol in ticker:

        close_value = yahooFinance.download(
            symbol, start=str(start_date), end=str(end_date)
        ).Close

        # We normalize the stock's close_value so that we can plot everything
        if normalize:

            ticker[symbol] = close_value / close_value.iloc[0] * 100
        else:
            ticker[symbol] = close_value

    return ticker


def plot_stocks(ticker):

    """
    Plots stock close values on a graph. No returns.

    Args:
        ticker: A dictionary with stock symbols as
        keys and stock close data as values

    """
    # Plot all the different stocks in the ticker
    # onto 1 graph
    for symbol in ticker:

        # We also label the graph to be the stock
        # symbol so that we can easily see on the legend
        # which line is which stock.
        ticker[symbol].plot(label=symbol)

    plt.ylabel("Stock price at Closing")
    plt.legend()
    plt.show()


def export_csv(ticker):
    """Autogenerates a csv file for each stock we track

    Args:
        ticker: a dictionary with ticker symbols as the keys and a
        Pandas Series object which holds the dates & closing prices
        as the values

    """
    for key, value in ticker.items():
        file_name = "".join([key, ".csv"])

        # Creates a CSV file for it
        value.to_csv(file_name, index=True)


def delta_values(ticker, date_span=1):
    """Finds the rate of change of
    stock prices day to day

    Args:
        ticker: a dictionary with ticker symbols as the keys and a
        Pandas Series object which holds the dates & closing prices
        as the values. The dictionary must have only 1 index.
        date_span: An integer which determines the spaces between the days.
        For example, date_span of 1 would mean that there is 1 day between each
        stock close price recorded. By default it is 1 one day.

    Returns:
        a Pandas Series of dates and rate of stock price changes"""

    delta = {}

    list_ticker = [(key, value) for key, value in ticker.items()]

    for i in range(1, len(list_ticker)):
        delta[list_ticker[i][0]] = list_ticker[i][1] - list_ticker[i - 1][1]

    return pd.Series(delta)
