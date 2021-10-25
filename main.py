# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import math
from scipy.stats import norm


def option_pricing(price, exercise_price, time_maturity):
    r = 0.01
    volatility = 0.43
    d1 = (math.log(price/exercise_price) + (r + (math.pow(volatility, 2)/2))*(time_maturity/360)) /\
         (volatility*math.sqrt((time_maturity/360)))
    d2 = d1 - (volatility*math.sqrt(time_maturity/360))

    return price * norm.cdf(d1) - exercise_price * math.pow(math.e, -(r*(time_maturity/360))) * norm.cdf(d2)


def asking_stock_price(ticker):
    api_token = 'c4ub5eqad3ie1t1fq6f0'
    url = f"https://finnhub.io/api/v1/quote?symbol={ticker.upper()}&token={api_token}"
    response = requests.get(url).json()

    return response['c']


if __name__ == '__main__':
    stock_ticker = input('Please enter the stock ticker: ')
    price = asking_stock_price(stock_ticker)
    print(stock_ticker.upper() + ' is currently trading at ' + str(price))
    exercise_price = float(input('Please enter the exercise price: '))
    time_maturity = float(input('Please enter the time to maturity (in days): '))
    print('The Option price for stock ' + stock_ticker.upper() + ' is: ' + str(option_pricing(price, exercise_price,
                                                                                              time_maturity)))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
