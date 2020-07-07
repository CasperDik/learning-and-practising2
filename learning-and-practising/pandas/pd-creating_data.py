#https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
import pandas as pd

#create the data with dictionary
data = {
    "apples": [3,2,0,1],
    "oranges": [0, 3, 7, 2]
}

purchases = pd.DataFrame(data)
purchases1 = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(purchases,"\n")
print(purchases1,"\n")

print(purchases1.loc["Robert"])
