import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

credits_frame = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

not_na = titles["imdb_score"].notna()
new_table = titles[not_na]
rated_movies = titles.loc[not_na & (titles["type"] == "MOVIE"), "imdb_score"]
rated_shows = titles.loc[not_na & (titles["type"] == "SHOW"), "imdb_score"]
print(rated_movies, rated_shows, rated_movies.mean(), rated_shows.mean(), sep="\n")

plt.subplot(1, 3, 1)

age_certification = titles[titles["type"] == "SHOW"]["age_certification"].dropna()
labels, values = np.unique(age_certification, return_counts=True)

plt.pie(values, labels=labels)

plt.subplot(1, 3, 2)
plt.hist(rated_movies, bins=np.arange(min(rated_movies), max(rated_movies) + 0.2, 0.2))

plt.subplot(1, 3, 3)
plt.hist(rated_shows, bins=np.arange(min(rated_shows), max(rated_shows) + 0.2, 0.2))
plt.show()
