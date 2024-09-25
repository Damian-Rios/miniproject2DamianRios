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

# Third chart (Histogram): Distribution of Audience Scores
# Pretty much the exact same as chart 2 but with audience scores instead of critic scores
# Getting data and plotting
plt.figure(figsize=(10, 6))
movies['audience_score'].hist(bins=25, color='#FFDE7A', edgecolor='black')

# Setting x-axis to start/end at edge
plt.xlim(0, 100)

# Setting up labels
plt.title('Distribution of Audience Scores')
plt.xlabel('Audience Score (%)')
plt.ylabel('Number of Movies')
plt.grid(False)

# Save plot as png
plt.savefig('charts/audience_score_distribution.png')
plt.show()

# Fourth chart (Scatter Plot): Critic vs Audience Scores
# Getting Random sample of movies
sample_size = 1000
sample_movies = movies.sample(n=sample_size)

# Getting data and creating plot with random sample
plt.figure(figsize=(10, 6))
plt.scatter(sample_movies['critic_score'], sample_movies['audience_score'], color='blue', alpha=0.5, label='Critic Scores')
plt.scatter(sample_movies['audience_score'], sample_movies['critic_score'], color='orange', alpha=0.5, label='Audience Scores')

# Setting up labels
plt.title('Critic Score vs Audience Score (Sampled)')
plt.xlabel('Critic Score (%)')
plt.ylabel('Audience Score (%)')
plt.legend()
plt.grid(True)

# Setting axis limits to start/end at edge
plt.xlim(0, 100)
plt.ylim(0, 100)

# Saving plot as png
plt.savefig('charts/critic_vs_audience_scatter_sampled.png')
plt.show()

# Fifth chart (Box Plot): Score Differences
# Getting Random sample of movies
sample_size = 500
sample_movies = movies.sample(n=sample_size)

# Calculating the score difference between audience and critics
sample_movies['score_difference'] = sample_movies['audience_score'] - sample_movies['critic_score']

# Checking for any NaN values and removing them
sample_movies = sample_movies.dropna(subset=['score_difference'])

# Plotting data in boxplot
plt.figure(figsize=(12, 8))
plt.boxplot(sample_movies['score_difference'], vert=False, showfliers=True)

# Setting up labels
plt.title('Score Difference (Audience - Critics) (Sampled)')
plt.xlabel('Score Difference (%)')
plt.grid(True)

# Calculating and setting x-axis limits
low_score = sample_movies['score_difference'].min() - (sample_movies['score_difference'].min() * 0.05)
high_score = sample_movies['score_difference'].max() + (sample_movies['score_difference'].max() * 0.05)
plt.xlim(low_score, high_score)

# Set x-axis to start and stop at low score and high score respectively
# Setting ticks to go by 5
plt.xticks(range(int(low_score), int(high_score) + 1, 5))

# Show summary statistics of sampled data
print("\nBoxplot Data (Audience - Critics) (Sampled)")
print("\nPositive values indicate audience scores are higher than critics.")
print("Negative values indicate critics rated higher than audiences.\n")
print(sample_movies['score_difference'].describe())

# Saving plot as png
plt.savefig('charts/score_difference.png')
plt.show()