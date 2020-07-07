#https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
import pandas as pd

movie_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")

print(movie_df.info())  #basic info about the dataset

print(movie_df.head())  #print first 5 rows
print(movie_df.tail(2))    #print last 2 rows

print(movie_df.shape)   # displays --> (rows,columns)

def drop_dupl():
    #create duplicates
    temp_df = movie_df.append(movie_df)
    print(temp_df.shape)

    #delete the duplicates
    temp_df.drop_duplicates(inplace=True)
    print(temp_df.shape)

drop_dupl()