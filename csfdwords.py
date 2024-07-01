import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cz_stopword_scrapped

'''
Top words
Average raiting
Average review lenght
Compare words to a rating
'''

sns.set_style('whitegrid')


def load_and_transform_data(filepath: str) -> pd.DataFrame:
    """
    Loads and transforms the data.
    """
    
    df = pd.read_csv(filepath)
    df['text'] = df['text'].str.lower()
    df['text'] = df['text'].str.replace(r'[().,!?-]', '', regex=True)
    df['label'] = df['label'].apply(lambda x: 'Positive' if x == 1 else 'Negative')
    
    return df

def plot_top_words(df: pd.DataFrame) -> None:
    """
    Plots the top words.
    """
    all_words = df['text'].str.split().explode()
    # Counting word occurrences
    word_counts = all_words.value_counts().reset_index()
    word_counts.columns = ['word', 'count']
    word_counts = word_counts.sort_values(by='count', ascending=False)
    top_words = word_counts.head(20)
    
    
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    sns.barplot(ax=ax1, data=top_words, x='count', y='word', palette='Spectral', hue='word')
    plt.imshow(ax=ax2, data=top_words)
    plt.show()
    print(top_words.head(50))

def review_lenght(df: pd.DataFrame) -> None:
    df['word_count'] = df['text'].str.split().apply(len)
    df['char_lenght'] = df['text'].apply(len)
    word_count_total = df['text'].str.split().count()
    
    unique_words = df['text'].str.split().explode()
    unique_word_count = set(unique_words)
    unique_word_count_total = len(unique_word_count)
    
    max
    
    df_grouped_rating = df.groupby(['label'])[['word_count', 'char_lenght']].mean().reset_index()
    print(word_count_total)
    print(df)
    print(df_grouped_rating)
    print("Total unique words:", unique_word_count_total)

def main() -> None:
    df = load_and_transform_data('train_data_csfd.csv')
    plot_top_words(df)
    # review_lenght(df)

main()