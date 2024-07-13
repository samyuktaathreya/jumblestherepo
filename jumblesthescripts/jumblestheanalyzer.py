#i want to make a graph of number of words jumbled everyday
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('jumblesthefiles\jumblesthedata.csv')

# Ensure 'date' column is in datetime format
df['date'] = pd.to_datetime(df['date'])

# Group by 'date' and count the number of words for each date
word_counts = df.groupby('date')['word'].count().reset_index()

# Rename columns for clarity
word_counts.columns = ['date', 'word_count']

# Filter out rows where word_count is 0
word_counts = word_counts[word_counts['word_count'] > 0]

# Plot the scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(word_counts['date'], word_counts['word_count'], color='blue')

# Add titles and labels
plt.title('Number of Words per Date')
plt.xlabel('Date')
plt.ylabel('Word Count')

# Format the x-axis to show only the year in the labels
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y'))
plt.gca().xaxis.set_major_locator(plt.matplotlib.dates.YearLocator())

# Rotate date labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.tight_layout()
plt.show()