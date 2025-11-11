Overview

The data/ folder is like the central storage hub for all datasets in our project. It contains:

Raw data collected from external sources (data_collection/)

Intermediate datasets after merging and cleaning

Final processed dataset ready for model prediction and visualization

Essentially, this folder is the pipeline’s “workspace”, holding every CSV the scripts generate or update. It allows each step of the pipeline to access the latest data without touching the original source code.

Key Points

Dynamic: Files are continuously updated whenever the pipeline runs.

Centralized: All raw, cleaned, and final datasets reside here.

Used by multiple scripts: main_data_pipeline.py, cleaning.py, and the final model scripts read/write from this folder.

Ready for visualization: The final CSV (final_disaster_data.csv) is what Tableau reads to show the world map visualization.

File-by-File Overview

twitter_data.csv

Raw tweets about disasters collected from Twitter.

Includes text, timestamp, user, etc.

newsapi_data.csv

Raw news articles fetched via NewsAPI.

Fields: title, description, content, source, timestamp.

reddit_data.csv

Disaster-related Reddit posts/comments.

Fields: title, text, url, created_utc, score, etc.

rss_data.csv

Disaster news from RSS feeds.

Fields: title, summary, link, published.

merged_data.csv

Combination of all raw datasets above.

Consolidates all text fields into combined_text.

Adds source_file to track origin.

Sorted by timestamp.

cleaned_dataset.csv

Cleaned version of merged_data.csv.

Text cleaned of URLs, special characters, extra spaces.

Location extracted using spaCy.

Only relevant columns retained: source, timestamp, clean_text, location.

final_disaster_data.csv

After applying the ML classification model and keyword-based hybrid boost.

Columns include:

timestamp

text (cleaned)

location

predicted_disaster_type

confidence

reason (model or keyword-assist)

This is the dataset used for Tableau visualization.
