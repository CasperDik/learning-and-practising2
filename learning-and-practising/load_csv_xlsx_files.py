import pandas as pd
import matplotlib.pyplot as plt

# read csv with pandas
dataset_1 = pd.read_csv("dataset1.csv")

print(dataset_1.head())

plt.plot(dataset_1["Date"], dataset_1["Close"])
plt.show()

# read xlsx with pandas
dataset_2 = pd.read_excel("dataset2.xlsx")

print(dataset_2.head())

plt.plot(dataset_2["Year"], dataset_2["Stock 1"])
plt.plot(dataset_2["Year"], dataset_2["Stock 2"])
plt.plot(dataset_2["Year"], dataset_2["Stock 3"])
plt.show()