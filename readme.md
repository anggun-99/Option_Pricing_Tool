This program calculates the price of a call and put option for a specific stock.

The calculation of the option price is based on the Black-Scholes-Merton model.

The prices of the stock can be obtained by an API. Whereas other information such as the exercise price, time to maturity, interest rates and the implied volatility will be obtained manually via user input.

The python statistic library scipy.stats is used to calculate the CDF (Cumulative distribution function) of a normal distribution. 
