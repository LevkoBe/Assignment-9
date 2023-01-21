import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

credits_frame = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

not_na = titles["imdb_score"].notna()
new_table = titles[not_na]
rated_movies = titles.loc[not_na & (titles["type"] == "MOVIE"), "imdb_score"]
rated_shows = titles.loc[not_na & (titles["type"] == "SHOW"), "imdb_score"]
print(rated_movies, rated_shows, sep="\n")

plt.subplot(1, 2, 1)
plt.hist(rated_movies, bins=np.arange(min(rated_movies), max(rated_movies), 0.2))

plt.subplot(1, 2, 2)
plt.hist(rated_shows, bins=np.arange(min(rated_shows), max(rated_shows), 0.2))
plt.show()
