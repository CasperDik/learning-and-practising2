#https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
import pandas as pd
import sqlite3

#csv
df = pd.read_csv("purchases.csv", index_col=0) #index_col sets column 0 as index column otherwise will create new index column
print(df, "\n")

#json
df1 = pd.read_json("purchases.json")
print(df1,  "\n")

#sql
con = sqlite3.connect("database.db")
df2 = pd.read_sql_query("SELECT * FROM purchases", con)
df2 = df2.set_index("index")  #can also do index_col
print(df2)

df.to_csv("new_purchases.csv")
df1.to_json("new_purchases.json")
df.to_sql("new_purchases", con)