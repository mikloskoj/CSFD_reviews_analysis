import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\janmi\OneDrive\My Work - All Files\imdb_top_1000.csv')

df = df.groupby(['Series_Title'])['IMDB_Rating'].mean().sort_values(ascending=False).head(30).reset_index()
print(df.to_string)

sns.set_style('whitegrid')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

sns.barplot(ax=ax1, data=df, x='Series_Title', y='IMDB_Rating', palette='viridis')

sns.histplot(ax=ax2, data=df, x='Series_Title', y='IMDB_Rating', palette='viridis')

ax2.set_xticklabels('')
ax1.set_xticklabels('')

plt.show()