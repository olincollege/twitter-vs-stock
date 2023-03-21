"""A class that organizes all the data nicely"""
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yahooFinance
from sklearn import preprocessing


class StockPlot:

    # Attributes
    def __init__(self, stock_name, start_date, end_date):
        self._ticker = stock_name
        self._start_date = start_date
        self._end_date = end_date

        self._stock_data = yahooFinance.download(
            self._ticker, start=str(self._start_date), end=str(self._end_date)
        ).Close

    # Getter Methods
    def get_stock_data(self):
        return self._stock_data

    def get_ticker(self):
        return self._ticker

    def create_csv(self):
        """Autogenerates a csv file for each stock we track. Pandas Series object which holds the dates & closing prices
        as the values"""

        file_name = "".join([self._ticker, ".csv"])
        # Creates a CSV file for it
        self._stock_data.to_csv(file_name, index=True)

    def get_normalized_data(self):
        prices_array = self._stock_data.values
        normalized_prices = preprocessing.normalize([prices_array])[0]
        print(normalized_prices[0])
        print(len(self._stock_data.index))
        return pd.Series(normalized_prices, self._stock_data.index)
