Real Time disaster aggregation model


Overview

This project is an end-to-end AI pipeline that collects, cleans, classifies, and visualizes real-world disaster-related data from multiple global sources. It provides a near real-time snapshot of disasters worldwide, helping authorities, NGOs, and analysts track trends and make informed decisions.


Objective

Design an AI-driven pipeline to collect, merge, clean, classify, and visualize disaster events from multiple sources, enabling a comprehensive, interactive global disaster monitoring system.

Data Collection Pipeline

Sources:

Twitter API: Real-time tweets containing disaster-related keywords

NewsAPI: Breaking news articles from verified sources

Reddit API: Community discussions and reports

RSS Feeds: Global disaster and environment channels

Each script (twitter_data.py, newsapi_data.py, reddit_data.py, rss_data.py) collects relevant posts and exports them as individual CSV files.

Integration:

main_data_pipeline.py automatically runs all data collection scripts and merges their outputs into a single dataset:

merged_data.csv — raw unified dataset (~270 entries from all platforms)

Data Cleaning & Enrichment

Script used: cleaning.py

Key Steps:

Combined all text-related columns (title, content, description, etc.) into combined_text

Removed duplicates, empty entries, and non-informative text

Normalized text:

Removed URLs, symbols, and special characters

Converted all text to lowercase

Extracted locations using spaCy NER (GPE, LOC, FAC entities)

Sorted data chronologically and standardized timestamps

Final Output:
cleaned_dataset.csv containing:

['source', 'timestamp', 'clean_text', 'location']

AI-Based Disaster Classification

Script used: hypomodel.ipynb

Functionality:

Runs cleaning.py to ensure up-to-date data

Loads pre-trained model and TF-IDF vectorizer:

disaster_classifier5.pkl

disaster_vectorizer3.pkl

Classification:

Predicts disaster type (Flood, Storm, Earthquake, Wildfire, etc.)

Hybrid logic combining ML predictions and keyword assistance

Each entry includes:

Predicted Disaster Type

Confidence Score

Source Reason (Model / Keyword Assist)

Final structured output:

final_disaster_data.csv

Visualization (Tableau Dashboard)

Method:

Visualizes final_disaster_data.csv on a world map

Each disaster entry plotted as a circle at its location

Interactive Features:

Hover tooltips: location, disaster type, timestamp, confidence, source

Color coding indicates disaster category

Dot size represents prediction confidence

Fully zoomable and pannable for regional exploration

Data Flow Summary
Data Sources → Merging → Cleaning → Classification → Visualization

Final Outcome

Gathers and merges real-time global data

Cleans and standardizes text intelligently

Classifies disaster events using ML and keyword logic

Visualizes global disaster patterns interactively

Impact

Helps authorities, NGOs, and analysts track disaster trends in near real-time

Supports early response and informed decision-making
