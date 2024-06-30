import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('rotten_tomatoes_movies.csv', sep=',', encoding='latin1')

df['original_release_date'] = pd.to_datetime(df['original_release_date'], format='%Y-%m-%d', dayfirst=True, errors='coerce')

df['original_release_year'] = df['original_release_date'].dt.year

fig, ax1 = plt.subplots(1, 1, figsize=(10, 8))

df_grouped = df.groupby(['original_release_year'])['movie_title'].count().reset_index()

sns.barplot(ax=ax1, data=df_grouped, x='original_release_year', y='movie_title')


plt.show()