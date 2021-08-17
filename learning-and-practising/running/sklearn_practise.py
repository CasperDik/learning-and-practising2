import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt

df1 = pd.read_csv("data/csv files/aggregated_running_data.csv")
df = df1[["speed", "heart_rate", "cadence", "timer(sec)", "distance", "temperature", "altitude", "run"]]
df = df.drop(df[df["timer(sec)"] < 60*3].index)
df = df.drop(df[df["speed"] < 1.5].index)

X = df[["heart_rate"]]
#X = df[["heart_rate", "cadence", "distance", "temperature", "altitude"]]
y = df[["speed"]]

reg = linear_model.LinearRegression().fit(X, y)
print("intercept: ", reg.intercept_)
print("coefficients: ", reg.coef_)
print("R2: ", reg.score(X, y))

predict = reg.predict(X)

plt.plot(X["heart_rate"], predict, label="predict", c="b")
plt.scatter(X["heart_rate"], y, label="true values", c="red")

plt.legend()
plt.show()
