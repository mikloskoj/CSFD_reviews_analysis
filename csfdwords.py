import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import cz_stopword_scrapped


sns.set_style('white')


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
    all_words = all_words[~all_words.isin(cz_stopword_scrapped.words)]
    all_words = all_words[~all_words.isin([':'])]
    # Counting word occurrences
    word_counts = all_words.value_counts().reset_index()
    word_counts.columns = ['word', 'count']
    word_counts = word_counts.sort_values(by='count', ascending=False) 
    top_words = word_counts.head(20)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'hspace': 0.5})
    
    sns.barplot(ax=ax1, data=top_words, x='count', y='word', palette='Spectral', hue='word')
    ax1.set_xlabel('')
    ax1.set_ylabel('')
    ax1.set_yticklabels(ax1.get_yticklabels(), fontsize=8, color='grey')
    ax1.set_xticklabels(ax1.get_xticklabels(), fontsize=8, color='grey')
    ax1.grid(color='lightgrey', linestyle='-', linewidth=0.25)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    
    ax1.text(0.5, 1.1, 'Top 20 Words', weight='bold', color='grey', ha='center', va='center', fontsize=12, transform=ax1.transAxes)
    ax1.text(0.5, 1.05, f'Czech most common stop words were excluded.', weight='normal', style='italic', color='grey', ha='center', va='center', transform=ax1.transAxes)
    
    table = ax2.table(cellText=top_words.values, colLabels=top_words.columns, loc='center')
    ax2.axis('off')
    ax2.grid(False)
    
    for key, cell in table.get_celld().items():
        cell.set_edgecolor('lightgrey')
        cell.set_linewidth(0.2)
        cell.set_text_props(weight='normal', color='grey', fontsize=8, ha='left', va='center')
        cell.set_height(0.05)
        if key[0] == 0:
            cell.set_text_props(weight='bold', color='grey', fontsize=7, ha='center', va='center')
            cell.set_facecolor('lightgrey')
            cell.set_height(0.1)
    
    plt.gcf().canvas.manager.set_window_title('Top 20 Words')
    plt.show()


def review_lenght(df: pd.DataFrame) -> None:
    df['word_count'] = df['text'].str.split().apply(len)
    df['char_lenght'] = df['text'].apply(len)
    word_count_total = df['text'].str.split().count()
    
    unique_words = df['text'].str.split().explode()
    unique_word_count = set(unique_words)
    unique_word_count_total = len(unique_word_count)
    
    df_grouped_rating = df.groupby(['label'])[['word_count', 'char_lenght']].mean().reset_index()

def main() -> None:
    df = load_and_transform_data('train_data_csfd.csv')
    plot_top_words(df)
    # review_lenght(df)

main()