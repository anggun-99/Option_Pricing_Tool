# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import math
from scipy.stats import norm


def check_float(input):
    try:
        val = float(input)
    except ValueError:
        print('Invalid input, please enter the correct number')
        return False
    return True


def check_integer(input):
    try:
        val = int(input)
    except ValueError:
        print("Invalid input, please enter an integer")
        return False
    return True


def call_option_pricing(price, exercise_price, time_maturity, r, volatility):
    d1 = (math.log(price/exercise_price) + (r + (math.pow(volatility, 2)/2))*(time_maturity/360)) /\
         (volatility*math.sqrt((time_maturity/360)))
    d2 = d1 - (volatility*math.sqrt(time_maturity/360))

    return price * norm.cdf(d1) - exercise_price * math.pow(math.e, -(r*(time_maturity/360))) * norm.cdf(d2)


def put_option_pricing(price, exercise_price, time_maturity, r, volatility):
    d1 = (math.log(price/exercise_price) + (r + (math.pow(volatility, 2)/2))*(time_maturity/360)) /\
         (volatility*math.sqrt((time_maturity/360)))
    d2 = d1 - (volatility*math.sqrt(time_maturity/360))

    return exercise_price * math.pow(math.e, -(r*(time_maturity/360))) * norm.cdf(-d2) - price * norm.cdf(-d1)


def asking_stock_price(ticker):
    api_token = 'c4ub5eqad3ie1t1fq6f0'
    url = f"https://finnhub.io/api/v1/quote?symbol={ticker.upper()}&token={api_token}"
    response = requests.get(url).json()

    return response['c']


if __name__ == '__main__':
    option_type = input('Please enter the option type: (call/put) ')

    if option_type == 'call':
        stock_ticker = input('Please enter the stock ticker: ')
        price = asking_stock_price(stock_ticker)
        print(stock_ticker.upper() + ' is currently trading at ' + str(price))

        check = False
        while check is False:
            exercise_price = input('Please enter the exercise price: ')
            check = check_float(exercise_price)
        exercise_price = float(exercise_price)

        check = False
        while check is False:
            time_maturity = input('Please enter the time to maturity (in days): ')
            check = check_integer(time_maturity)
        time_maturity = int(time_maturity)

        check = False
        while check is False:
            rates = input('Please enter the current interest rates: ')
            check = check_float(rates)
        rates = float(rates)

        check = False
        while check is False:
            volatility = input('Please enter the volatility: ')
            check = check_float(volatility)
        volatility = float(volatility)

        print('The ' + option_type + ' Option price for stock ' + stock_ticker.upper() + ' is: ' +
              str(call_option_pricing(price, exercise_price, time_maturity, rates, volatility)))

    if option_type == 'put':
        stock_ticker = input('Please enter the stock ticker: ')
        price = asking_stock_price(stock_ticker)
        print(stock_ticker.upper() + ' is currently trading at ' + str(price))

        check = False
        while check is False:
            exercise_price = input('Please enter the exercise price: ')
            check = check_float(exercise_price)
        exercise_price = float(exercise_price)

        check = False
        while check is False:
            time_maturity = input('Please enter the time to maturity (in days): ')
            check = check_integer(time_maturity)
        time_maturity = int(time_maturity)

        check = False
        while check is False:
            rates = input('Please enter the current interest rates: ')
            check = check_float(rates)
        rates = float(rates)

        check = False
        while check is False:
            volatility = input('Please enter the volatility: ')
            check = check_float(volatility)
        volatility = float(volatility)

        print('The ' + option_type + ' option price for stock ' + stock_ticker.upper() + ' is: ' +
              str(put_option_pricing(price, exercise_price, time_maturity, rates, volatility)))


# implied volatility of amd is 43.4%
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
