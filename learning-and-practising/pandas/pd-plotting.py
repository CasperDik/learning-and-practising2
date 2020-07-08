import pandas as pd
import matplotlib as plt

movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
movies_df.columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']

plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)})       #set fond and plot size

# plot
movies_df.plot(kind="scatter", x="rating", y="revenue_millions", title="Revenue vs rating")

plt.show()