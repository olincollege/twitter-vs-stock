"""Helper functions for getting and plotting stocks
using the Yfinance library"""

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yahooFinance
import StockPlot
from statistics import variance

from sklearn import preprocessing


def delta_values(stock1, stock2):
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

    delta = []

    for i in range(1, len(stock1)):
        delta.append(variance([stock1.values[i], stock2.values[i]]))

    return pd.Series(delta, stock1.index[1:])
