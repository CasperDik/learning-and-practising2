import numpy as np
import scipy.stats as si

# S: spot price
# K: strike price
# T: time to maturity
# r: interest rate
# d: rate of continuous dividend paying asset
# sigma: volatility of underlying asset

def euro_vanilla(S, X, T, r, sigma, option='call'):

    d1 = (np.log(S / X) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / X) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == "call":
        result = (S * si.norm.cdf(d1, 0.0, 1.0) - X * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == "put":
        result = (X * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))

    return result


def euro_vanilla_dividend(S, X, T, r, d, sigma, option='call'):
    d1 = (np.log(S / X) + (r - d + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / X) + (r - d - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if option == 'call':
        result = (S * np.exp(-d * T) * si.norm.cdf(d1, 0.0, 1.0) - X * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    if option == 'put':
        result = (X * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * np.exp(-d * T) * si.norm.cdf(-d1, 0.0, 1.0))

    return result
