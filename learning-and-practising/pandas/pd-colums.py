import pandas as pd

movie_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")

print(movie_df.columns)

#rename column names
movie_df.rename(columns={
        'Runtime (Minutes)': 'Runtime',
        'Revenue (Millions)': 'Revenue_millions'
    }, inplace=True)

print(movie_df.columns)

#rename all columns with list
movie_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']
print(movie_df.columns)

#rename all column name to lowercase
movie_df.columns = [col.lower() for col in movie_df]
print(movie_df.columns)