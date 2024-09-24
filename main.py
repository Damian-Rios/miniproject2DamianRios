### INF601 - Advanced Programming in Python
### Damian Rios
### Mini Project 2

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

movies = pd.read_csv("movie_info.csv")

# Convert data to floats
movies['critic_score'] = movies['critic_score'].str.replace('%', '').astype(float)
movies['audience_score'] = movies['audience_score'].str.replace('%', '').astype(float)

# Code to create charts folder
try:
    Path("charts").mkdir()
except FileExistsError:
    pass
