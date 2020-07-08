import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

# describe

print(movies_df.describe())         # get count, mean, std, min, max etc of the continuous variables
print(movies_df["revenue_millions"].describe())    # only for 1 variable
print(movies_df["genre"].describe())      # genre is categorical variable but also works then --> gives count, unique, top and freq of top values

print(movies_df["genre"].value_counts().head(10))       # frequency of all values in the column

# correlation

print(movies_df.corr())