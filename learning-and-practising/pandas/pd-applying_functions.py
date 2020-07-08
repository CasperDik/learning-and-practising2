import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

def rating_function(x):
    if x >= 8.0:
        return "good"
    else:
        return "bad"

movies_df["rating_category"] = movies_df["rating"].apply(rating_function)       #apply defined function on rating and create new column called "rating category"

#or with lamda
movies_df["rating_category"] = movies_df["rating"].apply(lambda x: 'good' if x >= 8.0 else 'bad')



