"""Helper functions for getting and plotting stocks
using the Yfinance library"""

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yahooFinance
import StockPlot
from statistics import variance

from sklearn import preprocessing


def list_merger(stock_list, func="get_stock_data"):
    """Finds the Pearson Coefficient from percent variance


    Args:
        stock_list:

    Returns:
        a Pandas Series of dates and rate of stock price changes"""

    if func == "get_variance_data":
        data = [stock.get_variance_data() for stock in stock_list]
    else:
        data = [stock.get_stock_data() for stock in stock_list]

    # Merging the lists into 1 Pandas Dataframe
    name_list = [stock.get_ticker() for stock in stock_list]
    merged_frame = pd.concat(data, axis=1)
    named_frame = merged_frame.set_axis(name_list, axis=1)

    return named_frame


def filterer(stock_list):
    """Finds the Pearson Coefficient from percent variance


    Args:
        stock_list:

    Returns:
        a Pandas Series of dates and rate of stock price changes"""

    # Merging the lists into 1 Pandas Dataframe
    variance_list = [stock.get_variance_data() for stock in stock_list]
    name_list = [stock.get_ticker() for stock in stock_list]
    merged_frame = pd.concat(variance_list, axis=1)
    named_frame = merged_frame.set_axis(name_list, axis=1)

    return named_frame
