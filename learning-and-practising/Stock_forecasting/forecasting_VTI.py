# https://www.kaggle.com/mtszkw/xgboost-for-stock-trend-prices-prediction
# see comment of author --> test data should include all time high of a time series
# todo: make own model, different predictors
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import xgboost as xgb
from xgboost import plot_importance
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV

df = pd.read_csv("Unilever_5yhistorical.csv")
df_close = df[['Date', 'Close']].copy()
df_close = df_close.set_index('Date')

# create inputs for model
# EMA=exponential MA, SMA=simple MA
df["EMA_9"] = df["Close"].ewm(9).mean().shift()
df["SMA_5"] = df["Close"].rolling(5).mean().shift()
df["SMA_10"] = df["Close"].rolling(10).mean().shift()
df["SMA_15"] = df["Close"].rolling(15).mean().shift()
df["SMA_30"] = df["Close"].rolling(30).mean().shift()

# Relative strength index = momentum indicator
def RSI(df, n=14):
    close = df["Close"]
    delta = close.diff()[1:]
    pricesUp = delta.copy()
    pricesUp[pricesUp < 0] = 0
    pricesDown = delta.copy()
    pricesDown[pricesDown > 0] = 0
    rollUp = pricesUp.rolling(n).mean()
    rollDown = pricesDown.abs().rolling(n).mean()
    rs = rollUp / rollDown
    rsi = 100.0 - (100.0 / (1.0 + rs))
    return rsi

df["RSI"] = RSI(df)

# MACD - Moving average convergence divergence - trend-following momentum indicator
EMA_12 = pd.Series(df["Close"].ewm(span=12, min_periods=12).mean())
EMA_26 = pd.Series(df["Close"].ewm(span=26, min_periods=26).mean())
df["MACD"] = pd.Series(EMA_12 - EMA_26)
df["MACD signal"] = pd.Series(df.MACD.ewm(span=9, min_periods=9).mean())

# predict next day thus shift --> now have price of t+1, linked to indicators of time t
df['Close'] = df['Close'].shift(-1)
df = df.iloc[33:]   # Because of moving averages and MACD line
df = df[:-1]      # Because of shifting close price

# split this dataset into 60% train, 20% validation, and 20% test
df.index = range(len(df))
test_size = 0.15
valid_size = 0.15
test_split_idx = int(df.shape[0] * (1-test_size))
valid_split_idx = int(df.shape[0] * (1-(valid_size+test_size)))

train_df = df.loc[:valid_split_idx].copy()
valid_df = df.loc[valid_split_idx+1:test_split_idx].copy()
test_df = df.loc[test_split_idx+1:].copy()

# drop unnecessary columns
drop_columns = ["Date", "Volume", "Open", "Low", "High", "Adj Close"]

train_df = train_df.drop(drop_columns, 1)
valid_df = valid_df.drop(drop_columns, 1)
test_df = test_df.drop(drop_columns, 1)

# get y and drop from X
y_train = train_df["Close"].copy()
X_train = train_df.drop(["Close"], 1)

y_valid = valid_df["Close"].copy()
X_valid = valid_df.drop(["Close"], 1)

y_test = test_df["Close"].copy()
X_test = test_df.drop(["Close"], 1)

# finetune XGboost regressor
parameters = {
    'n_estimators': [100, 200, 300, 400],
    'learning_rate': [0.001, 0.005, 0.01, 0.05],
    'max_depth': [8, 10, 12, 15],
    'gamma': [0.001, 0.005, 0.01, 0.02],
    'random_state': [42]
}

eval_set = [(X_train, y_train), (X_valid, y_valid)]
model = xgb.XGBRegressor(eval_set=eval_set, objective='reg:squarederror', verbose=False)
clf = GridSearchCV(model, parameters)

clf.fit(X_train, y_train)
print(f'Best params: {clf.best_params_}')
print(f'Best validation score = {clf.best_score_}')

model = xgb.XGBRegressor(**clf.best_params_, objective='reg:squarederror')
model.fit(X_train, y_train, eval_set=eval_set, verbose=False)
plot_importance(model)
plt.show()

y_pred = model.predict(X_test)
print(f'y_true = {np.array(y_test)[:5]}')
print(f'y_pred = {y_pred[:5]}')

print(f'mean_squared_error = {mean_squared_error(y_test, y_pred)}')

predicted_prices = df.loc[test_split_idx+1:].copy()
predicted_prices["Close"] = y_pred

plt.plot(predicted_prices["Date"], predicted_prices["Close"], label="Prediction", c="red")
plt.plot(df["Date"], df["Close"], label="actual", c="blue")
plt.legend()
plt.show()

plt.plot(predicted_prices["Date"], predicted_prices["Close"], label="Prediction", c="red")
plt.plot(predicted_prices["Date"], y_test, label="actual", c="blue")
plt.legend()
plt.show()
