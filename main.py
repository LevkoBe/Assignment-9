import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

credits_frame = pd.read_csv("credits.csv")
titles = pd.read_csv("titles.csv")

# first part

rated_movies = titles[titles["type"] == "MOVIE"]["imdb_score"].dropna()
rated_shows = titles[titles["type"] == "SHOW"]["imdb_score"].dropna()

plt.figure(figsize=(13, 8))

plt.subplot(2, 2, 1)
sns.histplot(titles, x="imdb_score", bins=np.arange(0, 10.2, 0.2), hue="type")
plt.xlabel("Score")
plt.ylabel("Amount")
plt.axvline(rated_movies.mean(), color="k", linestyle='dashed', linewidth=1)
plt.axvline(rated_shows.mean(), color="#123456", linestyle='dashdot', linewidth=1)

# second part

plt.subplot(2, 2, 2)
age_certifications = titles[titles['type'] == 'SHOW']['age_certification'].dropna()
labels, values = np.unique(age_certifications, return_counts=True)
plt.pie(values, labels=labels)

# fourth part
top_1000 = titles.sort_values(by="imdb_score", ascending=False).head(1000)
double_table = pd.merge(top_1000, credits_frame[credits_frame['role'] == "ACTOR"], how="inner", on=["id"])
actor_rating = double_table.groupby(by="name")['title'].count().sort_values(ascending=False).head(10)

print(titles.groupby(by=["type"])["imdb_score"].mean())

# fifth part

genres_for_movie = top_1000[top_1000['type'] == 'MOVIE']
genres_for_show = top_1000[top_1000['type'] == 'SHOW']
list_of_chars = ['[', ']', "'", ' ']
translation_table = str.maketrans('', '', ''.join(list_of_chars))
all_genres_for_movie = [x.translate(translation_table).split(',') for x in genres_for_movie['genres']]
all_genres_for_show = [x.translate(translation_table).split(',') for x in genres_for_show['genres']]
movie_genres = {}
show_genres = {}

for current_list in all_genres_for_movie:
    for genre in current_list:
        if genre not in movie_genres:
            movie_genres[genre] = 0 
        movie_genres[genre] += 1


for current_list in all_genres_for_show:
    for genre in current_list:
        if genre not in show_genres:
            show_genres[genre] = 0 
        show_genres[genre] += 1

# .to_frame()
df1 = pd.DataFrame({'type': list(movie_genres.keys()), 'value': list(movie_genres.values())})
df2 = pd.DataFrame({'type': list(show_genres.keys()), 'value': list(show_genres.values())})
double_array = pd.merge(df1, df2, how="outer", on='type')

plt.subplot(2, 2, 3)
plt.barh(df1['type'], df1['value'])
plt.xlabel("movie")

plt.subplot(2, 2, 4)
plt.barh(df2['type'], df2['value'])
plt.xlabel("show")


plt.show()
