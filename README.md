### INF601 - Advanced Programming in Python
### Damian Rios
### Mini Project 2


# Mini Project 2

## Description
This project analyzes a dataset of movie ratings from Rotten Tomatoes, comparing critic scores to audience scores.
The data is visualized using various charts and plots generated with Matplotlib.
The analysis includes bar charts, histograms, scatter plots, and box plots, allowing users to
explore the relationship between critic and audience ratings, and identify any notable differences.


## Getting Started

### Dataset
You can download the dataset used for this project from the following link:
[Movie Ratings Dataset](https://www.reddit.com/r/datasets/comments/1ecj6m2/dataset_for_rotten_tomatoes_movies_1970_2024/)

Make sure to place the downloaded file in the root directory of the project
and name it `movie_info.csv` before running the program.

### Dependencies
Make sure all required libraries are installed by running:
```
pip install -r requirements.txt
```

### Executing program
In a terminal window, please type the following command to execute the program:
```
python main.py
```

### Output
The program will produce the following charts:

1. Comparison of Critic and Audience Scores (Bar Chart): Visualizes the difference between critic and audience scores for a random sample of movies.

2. Distribution of Critic Scores (Histogram): Shows the distribution of critic scores in the dataset.

3. Distribution of Audience Scores (Histogram): Shows the distribution of audience scores in the dataset.

4. Critic vs Audience Scores (Scatter Plot): Compares critic and audience scores for a random sample of movies, using different colors to represent the two.

5. Score Differences (Box Plot): Visualizes the differences between audience and critic scores of a random sample using a box plot.

These visualizations are saved as PNG files in the charts folder and updated with each run of the program.


## Authors

Damian Rios

## Acknowledgments

Inspiration, code snippets, etc.
* [Pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/index.html)
* [Pandas-random sample](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#selecting-random-samples)
* [Pandas-dropna()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna)
* [Matplotlib-charts/plots](https://matplotlib.org/stable/tutorials/pyplot.html)
* [Matplotlib-plot formating](https://matplotlib.org/stable/users/explain/quick_start.html#labelling-plots)
* [Matplotlib-Boxplot](https://matplotlib.org/stable/gallery/statistics/boxplot_demo.html#sphx-glr-gallery-statistics-boxplot-demo-py)
* [Textwrap module](https://docs.python.org/3/library/textwrap.html)

