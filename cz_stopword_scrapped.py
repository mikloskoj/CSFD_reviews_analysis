import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage
url = "https://nlp.fi.muni.cz/cs/StopList"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table rows
rows = soup.find_all('tr')

# Initialize lists to store the table data
words = []
mid_sentence_freq = []
start_sentence_freq = []
total_freq = []
percentage_start_sentence = []

# Iterate over the rows to extract the data
for row in rows[1:]:  # Skipping the header row
    cols = row.find_all('td')
    words.append(cols[0].text.strip())
    mid_sentence_freq.append(float(cols[1].text.strip().replace(',', '.')))
    start_sentence_freq.append(float(cols[2].text.strip().replace(',', '.')))
    total_freq.append(float(cols[3].text.strip().replace(',', '.')))
    percentage_start_sentence.append(float(cols[4].text.strip().replace(',', '.')))

# Create a DataFrame
df = pd.DataFrame({
    'Word': words,
    'Mid Sentence Frequency': mid_sentence_freq,
    'Start Sentence Frequency': start_sentence_freq,
    'Total Frequency': total_freq,
    'Percentage Start Sentence': percentage_start_sentence
})

# Display the DataFrame
print(df.head())