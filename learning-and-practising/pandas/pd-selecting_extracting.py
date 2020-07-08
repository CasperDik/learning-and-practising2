import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

    # extracting by column
subset = movies_df[['genre', 'rating']]

    # extracting by row

# 2 options by name or by numerical index
prom = movies_df.loc["Prometheus"]      # by name-> movie title in this case
prom1 = movies_df.iloc[1]                # by numerical index

# multiple rows
movie_subset = movies_df.loc['Prometheus':'Sing']   # from Prometheus till Sing
movie_subset1 = movies_df.iloc[1:4]     # does not include movie at index 4

    # conditional selection

condition = movies_df[movies_df['director'] == "Ridley Scott"]       # only movies directed by Ridley Scott

condition1 = movies_df[movies_df['rating'] >= 8.6]                    # only movies with 8.6 or higher

# multiple conditions   --> |=or, &=and
cond = movies_df[(movies_df['director'] == 'Christopher Nolan') | (movies_df['director'] == 'Ridley Scott')]

# or
cond1 = movies_df[movies_df['director'].isin(['Christopher Nolan', 'Ridley Scott'])]

# all movies that were released between 2005 and 2010,
# have a rating above 8.0, but
# made below the 25th percentile in revenue.

condition2 = movies_df[
    ((movies_df['year'] >= 2005) & (movies_df['year'] <= 2010))
    & (movies_df['rating'] > 8.0)
    & (movies_df['revenue_millions'] < movies_df['revenue_millions'].quantile(0.25))
]
