import statistics
import numpy as np
stock_price = [100,102,98,105,101,97,99,103,100,98]
variance = statistics.variance(stock_price)
print(f"Variance of stock prices:(variance)")
numpy_variance = np.var(stock_price,ddof=1)
print(f"Varinace of stock_prices (using Numpy): {numpy_variance}")