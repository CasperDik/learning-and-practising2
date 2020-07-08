import pandas as pd
from matplotlib import pyplot as plt

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

# plot
movies_df.plot(kind="scatter", x="rating", y="revenue_millions", title="Revenue vs rating")
plt.show()