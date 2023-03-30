"""A class that organizes all the stock data """
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

    def get_variance_data(self, data_type="raw"):
        """Calculates the percent variance (%) of the closing prices between
        dates

        Return:
            A Pandas dataframe which contains the percent variance between
            two dates
        """
        deltas = [0]

        if data_type == "raw":
            prices_array = self.get_stock_data()
        if data_type == "normalized":
            prices_array = self.get_normalized_data()

        for i in range(1, len(prices_array)):
            delta_price = prices_array[i] - prices_array[i - 1]
            delta_price = delta_price / prices_array[i - 1]
            deltas.append(delta_price * 100)

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

    def get_range_date(self, interest_date, range_date=9, type="raw"):
        """Gets a range of dates & stock prices from the overall
        stock data in the class with a chosen date of interest
        being in the middle

        Args:
            interest_date: String which represents the date of interest
            in the format YYYY-MM-DD.
            range_date: An integer number n which represents number of dates
            n days before and n days after the interest_date
            type: A Pandas Dataframe which identifies what "overall stock data"
            we're looking at. This way we can change whether we're looking for
            raw, normalized, or percent variance stock data.ff

        Return:
            A Pandas Dataframe which contains stock & date data with a
            total length range_date *2 +1 with the date in the middle
            being the interest_date.
            If the interest_date is not in the self._stock_data range
            then it will return None"""

        df_types = {
            "raw": self.get_stock_data(),
            "normalized": self.get_normalized_data(),
            "variance": self.get_variance_data(),
        }

        # Error Catches
        try:
            dataframe = df_types[type]
        except KeyError:
            print(
                f"{type} is an invalid type argument value. You can choose from"
                " raw, normalized, or variance. type arguement will default to"
                " raw stock data"
            )
            dataframe = df_types["raw"]

        for i in range(len(dataframe) - 1):
            if dataframe[i : i + 1].index == interest_date:
                # Makes sure the parameters don't start in the
                # negative index.
                first_date = max(i - range_date, 0)
                # Makes sure the parameters don't go over index. The +1
                # compensates for the nature of string splicing
                last_date = min(i + range_date + 1, len(dataframe))

                return dataframe[first_date:last_date]

        print("The date of interest is not in the range of stock data")
        return dataframe
