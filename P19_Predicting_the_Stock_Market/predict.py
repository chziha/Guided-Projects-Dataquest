import pandas as pd
from datetime import datetime

df_stock = pd.read_csv("sphist.csv")
df_stock["Date"] = pd.to_datetime(df_stock["Date"])
df_stock.sort_values(by = ["Date"], ascending=True, inplace = True)

df_stock["avg_5"] = pd.rolling_mean(df_stock["Close"], window = 5).shift(1)
df_stock["avg_30"] = pd.rolling_mean(df_stock["Close"], window = 30).shift(1)
df_stock["avg_365"] = pd.rolling_mean(df_stock["Close"], window = 365).shift(1)

df_stock["std_5"] = pd.rolling_std(df_stock["Close"], window = 5).shift(1)
df_stock["std_365"] = pd.rolling_std(df_stock["Close"], window = 365).shift(1)

df_stock["ratio_avg"] = df_stock["avg_5"] / df_stock["avg_365"]
df_stock["ratio_std"] = df_stock["std_5"] / df_stock["std_365"]

df_stock = df_stock[df_stock["Date"] > datetime(year=1951, month=1, day=2)]
df_stock.dropna(axis = 0, inplace = True)

train = df_stock[df_stock["Date"] < datetime(year=2013, month=1, day=1)]
test = df_stock[df_stock["Date"] >= datetime(year=2013, month=1, day=1)]

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

model_lr = LinearRegression()
model_lr2 = LinearRegression()

features_cols = ["avg_5", "avg_30", "avg_365", "std_5", "std_365", "ratio_avg", "ratio_std"]
features_cols2 = ["avg_5", "avg_365", "std_5", "std_365"]

model_lr.fit(train[features_cols], train["Close"])
predictions = model_lr.predict(test[features_cols])

model_lr2.fit(train[features_cols2], train["Close"])
predictions2 = model_lr2.predict(test[features_cols2])

mse = mean_squared_error(test["Close"], predictions)
mse2 = mean_squared_error(test["Close"], predictions2)

print("mse is ", mse)
print("mse2 is ", mse2)