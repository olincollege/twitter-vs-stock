"""A class that organizes all the data nicely"""
import pandas as pd
import yfinance as yahooFinance
from sklearn import preprocessing


class StockPlot:
    """A simple class which handles web scraping from Yahoo Finance
    and generates various permutations of the stock closing values.

    Attributes:
        _ticker = a string that is the stock's official symbol
        _start_date = a string that is start date for the range
        of time we want to scrape between. Format is YYYY-MM-DD
        _end_date = a string that is the end date for the range
        of time we want to scrape between. Format is YYYY-MM-DD
        _stock_data = A Pandas Dataframe which contains the
        date & stock closing value web-scraped from Yahoo
        Finance ranging from the _start_date to the _end_date

    """

    def __init__(self, stock_name, start_date, end_date):
        self._ticker = stock_name
        self._start_date = start_date
        self._end_date = end_date

        self._stock_data = yahooFinance.download(
            self._ticker, start=str(self._start_date), end=str(self._end_date)
        ).Close

    # Getter Methods
    def get_stock_data(self):
        """A getter method for stock data

        Return:
            A Panda Dataframe that contains
        the date and the raw stock closing prices"""
        return self._stock_data

    def get_ticker(self):
        """A getter method for the stock ticker symbol

        Return:
            A string that is the stock ticker symbol"""
        return self._ticker

    def create_csv(self):
        """Autogenerates a csv file for the stocks & dates.

        Return:
            Pandas Series object which holds the dates & closing prices
        as the values"""

        file_name = "".join([self._ticker, ".csv"])
        # Creates a CSV file for it
        self._stock_data.to_csv(file_name, index=True)

    def get_variance_data(self, data_type="raw"):
        """Calculates the percent variance of the closing prices between
        dates

        Return:
            A Pandas dataframe which contains the percent variance between
            two dates
        """
        deltas = [0]

        if data_type == "raw":
            prices_array = self._stock_data
        if data_type == "normalized":
            prices_array = self.get_normalized_data()

        for i in range(1, len(prices_array)):
            delta_price = prices_array[i] - prices_array[i - 1]
            delta_price = delta_price / prices_array[i - 1]
            deltas.append(delta_price)

        return pd.Series(deltas[1:], self._stock_data.index[1:])

    def get_normalized_data(self):
        """Scales the values of stocks to between 0-1 while preserving
        the stock's overall behavior

        Return:
            A Pandas dataframe which contains the normalized version
             of the stock's closing prices
        """
        prices_array = self._stock_data.values
        normalized_prices = preprocessing.normalize([prices_array])[0]
        return pd.Series(normalized_prices, self._stock_data.index)
