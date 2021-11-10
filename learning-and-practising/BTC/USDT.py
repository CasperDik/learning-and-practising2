import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

df = pd.read_csv("data_usdt_btc.csv")

date = df["date"]
pch_btc = df["BTC close"].pct_change()
pch_usdt_supply = df["Market Cap"].pct_change()

i = 365
y = pch_btc.rolling(i).mean().shift()[i+1:].to_numpy()
X = pch_usdt_supply.rolling(i).mean().shift()[i+1:].to_numpy()

reg = LinearRegression().fit(X[:, None], y)
print("R2 ", reg.score(X[:, None], y))
print("Coefficients ", reg.coef_)
print("Intercept ", reg.intercept_)
predict = reg.predict(X[:, None])

plt.scatter(X, y)
plt.plot(X, predict)
plt.show()
