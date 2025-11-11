Overview

The model.build/ folder is the processing & cleaning powerhouse of your pipeline.
It doesn’t collect raw data like data_collection/ or store final results like data/. Instead, it prepares the data so the model can understand it and make accurate predictions.

Think of it as the “kitchen”: raw ingredients (datasets) come in, they are chopped, cleaned, and prepped, and then passed to the “chef” (your ML model) to cook the final dish.

Key Points

Runs after raw data is collected: Depends on merged_data.csv from data/.

Prepares text for ML: Combines columns, cleans text, removes noise, extracts locations.

Generates cleaned dataset: Output is cleaned_dataset.csv in data/.

Handles errors and edge cases: Ensures timestamps are standardized, missing data is managed, and text columns exist.

Supports multi-source data: Works for Twitter, NewsAPI, Reddit, RSS feeds, etc.

File Overview

cleaning.py

Purpose: Cleans the merged dataset and extracts relevant info.

Steps it performs:

Runs main_data_pipeline.py to ensure merged_data.csv exists.

Loads merged dataset and identifies the timestamp column.

Combines text columns (title, description, text, content, summary) into combined_text.

Cleans text (removes URLs, special characters, extra spaces).

Uses spaCy to extract locations (GPE, LOC, FAC) from text.

Sorts data by timestamp.

Keeps only relevant columns: source, timestamp, clean_text, location.

Saves cleaned_dataset.csv in data/ for model use.
