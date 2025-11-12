MyNextMovie Recommender System
Overview

This project builds an intelligent movie recommendation system using data analysis and machine learning techniques. The system helps users discover new movies based on their previous preferences and the behavior of similar users.

Datasets

movies.csv: Contains movie details such as ID, title, and genres.

ratings.csv: Contains user ratings with fields like userId, movieId, rating, and timestamp.

Tools & Libraries

Python

Pandas, NumPy: Data manipulation and cleaning

Matplotlib, Seaborn: Visualization and exploratory data analysis

Scikit-learn: Building and evaluating recommendation algorithms

Workflow
1. Data Loading & Cleaning

Imported and validated both datasets.

Converted timestamps into human-readable format.

Checked for missing or duplicate values.

Counted total unique users, movies, and ratings.

2. Exploratory Data Analysis (EDA)

Visualized rating distributions and top-rated movies.

Identified popular genres and user rating patterns.

Analyzed biases in rating behavior and user activity frequency.

3. Feature Engineering

Extracted and encoded movie genres into multiple categories.

Merged movie and rating data to create a comprehensive user–movie matrix.

4. Recommendation Techniques

Popularity-Based: Suggested movies with the highest ratings or number of reviews.

Collaborative Filtering (Memory-Based): Recommended movies using user–user or item–item similarity (cosine similarity/correlation).

Model-Based (Optional): Applied matrix factorization (SVD) for predicting unknown ratings.

5. Evaluation

Compared predicted recommendations against real user preferences.

Used metrics such as RMSE or MAE to measure model performance.

Key Insights

Most movies receive ratings between 3 and 4, showing users tend to rate positively.

Action, Drama, and Comedy emerged as the most common genres.

A small fraction of active users contributes a large share of ratings.

The system shows a popularity bias, often recommending well-known titles.

Collaborative filtering provides personalized movie suggestions based on user similarity.
