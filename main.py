### INF601 - Advanced Programming in Python
### Damian Rios
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import textwrap

movies = pd.read_csv("movie_info.csv")

# Convert data to floats
movies['critic_score'] = movies['critic_score'].str.replace('%', '').astype(float)
movies['audience_score'] = movies['audience_score'].str.replace('%', '').astype(float)

# Code to create charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass

# First chart (Bar Chart): Comparison of Critic and Audience Scores
# number of random rows of data to choose
sample_size = 15
sample_movies = movies.sample(n=sample_size)

# Getting data to plot
sample_movies[['critic_score', 'audience_score']].plot(kind='bar', figsize=(12, 6))

# Wrap movie titles using textwrap for better layout
wrapped_titles = [textwrap.fill(title, width=15) for title in sample_movies['title']]

# Setting up chart labels
plt.title('Comparison of Critic and Audience Scores (Sampled)')
plt.ylabel('Score (%)')
plt.xlabel('Movies')
plt.legend(title='Score Type')

# Formating x-axis so it looks better
plt.xticks(ticks=range(sample_size), labels=wrapped_titles, rotation=45, ha='center')

plt.tight_layout()

# Save plot as png
plt.savefig('charts/critic_audience_comparison.png')
plt.show()

# Second chart (Histogram): Distribution of Critic Scores
# Getting data and plotting
plt.figure(figsize=(10, 6))
movies['critic_score'].hist(bins=25, color='skyblue', edgecolor='black')

# Setting x-axis to start/end at edge
plt.xlim(0, 100)

# Setting up labels
plt.title('Distribution of Critic Scores')
plt.xlabel('Critic Score (%)')
plt.ylabel('Number of Movies')
plt.grid(False)

# Save plot as png
plt.savefig('charts/critic_score_distribution.png')
plt.show()