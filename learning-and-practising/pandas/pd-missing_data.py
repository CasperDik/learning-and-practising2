import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

    # dropping nulls

print(movies_df.isnull())       # check for each data point if null(missing variable)
print(movies_df.isnull().sum())     # number of nulls per column

movies_df.dropna()      # drop all rows with null values

movies_df.dropna(axis=1)    # drop columns with null values - axis=1 comes from .shape(=tuple) where 0 is row en 1 is column


    # imputation - replacing null with input

# extract column with missing nulls into own variable
revenue = movies_df["revenue_millions"]
print(revenue.head())

# get mean revenue as variable
mean_revenue = revenue.mean()

# replace nulls with mean value
revenue.fillna(mean_revenue, inplace=True)      # inplace affects main data set --> movies_df

print(movies_df.isnull().sum())

# describe
print(movies_df.describe())         # get count, mean, std, min, max etc of the continuous variables
print(movies_df["revenue_millions"].describe())    # only for 1 variable
print(movies_df["genre"].describe())      # genre is categorical variable but also works then --> gives count, unique, top and freq of top values

print(movies_df["genre"].value_counts().head(10))       # frequency of all values in the column

