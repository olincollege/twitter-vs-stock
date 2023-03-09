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


def get_close_stocks(ticker, start_date, end_date):
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
        ticker[symbol] = close_value / close_value.iloc[0] * 100

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
