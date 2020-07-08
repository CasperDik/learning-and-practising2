import pandas as pd
from matplotlib import pyplot as plt

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

movies_df["rating_category"] = movies_df["rating"].apply(lambda x: 'good' if x >= 8.0 else 'bad')

# plot
movies_df.plot(kind="scatter", x="rating", y="revenue_millions", title="Revenue vs rating")

movies_df['rating'].plot(kind='hist', title='Rating')

movies_df['rating'].plot(kind="box")

movies_df.boxplot(column='revenue_millions', by='rating_category')

plt.show()