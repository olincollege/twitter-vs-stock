"""
Tests for the stock_plot class & its methods
Note that because stock_plot is a class we will 
need to create an instance of it for testing
purposes

"""
import pytest
import stock_plot as sp
import pandas as pd
import yfinance as yahooFinance
from sklearn import preprocessing

GET_TICKER_CASES = [
    # Ticker Exists
    "AAPL",
    # Ticker Exists but has non alphabetical symbols
    "^NDX",
    # Ticker with numbers but doesn't exist
    "1234",
    # A ticker that doesn't exist
    "ASASSASAS",
]

GET_STOCK_DATA_CASES = [
    # ticker & start & end dates are all correct
    (["AAPL", "2018-02-11", "2019-11-11"], False),
    # Ticker doesn't exist
    (["^2NXSSSS", "2018-02-11", "2019-11-11"], True),
    # start date is older than end date
    (["AAPL", "2030-02-11", "2019-11-11"], True),
    # Start date isn't formatted right
    (["AAPL", "2018--11", "2019-11-11"], True),
    # End date isn't formatted right
    (["AAPL", "2018-02-11", "2019--11"], True),
    # start & end dates aren't strings
    (["AAPL", 2018 - 2 - 11, 2019 - 11 - 11], True),
    # The start date is before the stock existed.
    # Should just grab from the when the stock IPOed
    # and continues
    (["AAPL", "1950-05-11", "2019-11-11"], False),
    # Date with non-numerical values
    (["AAPL", "195S-0a-11", "2019-11-11"], True),
]


@pytest.mark.parametrize("ticker", GET_TICKER_CASES)
def test_get_ticker(ticker):
    """Tests that our get_ticker() function works.

    If the ticker inputted when initializing our
    StockPlot class isn't a string or empty,
    the entire class will fail, so we're just testing
    whether the get_ticker() function will still return
    the same string ticker that was inputted.

    Args:
        ticker: A string which represents the stock's
        ticker symbol and  will go into the
        instance's ticker parameter."""

    SET_DATE1 = "2021-11-08"
    SET_DATE2 = "2022-11-08"

    stock = sp.StockPlot(ticker, SET_DATE1, SET_DATE2)

    assert stock.get_ticker() == ticker


@pytest.mark.parametrize("stock,key", GET_STOCK_DATA_CASES)
def test_get_stock_data(stock, key):
    """We test whether we were able to make a successful yfinance web scrape
    download based on the Pandas series generated that contains all the stock
    data that was web scraped

    Args:
        stock: A list with a length of 3. The first index contains the stock ticker,
        the second index contains the start date, and the third index has the end date.
        Each index does not have to be a string, but it generally is.
        key: A boolean which indicates when getting stock data wasn't successful.
    """
    test_stock = sp.StockPlot(stock[0], stock[1], stock[2])
    # Stock retrieval was unsuccessful if
    # stock.get_stock_data() is an empty Series
    assert test_stock.get_stock_data().empty == key
