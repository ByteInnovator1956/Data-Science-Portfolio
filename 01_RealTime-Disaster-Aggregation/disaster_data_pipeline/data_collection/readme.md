Overview

This folder is responsible for fetching raw disaster-related data from multiple external sources. Each script is independent, targeting a specific data source (social media, news, RSS feeds).

The purpose of this folder is to collect fresh, relevant disaster data automatically and save it as CSV files in the data/ folder, which are later merged and processed by the pipeline.

All scripts export their results as .csv in data/:

twitter_data.csv

newsapi_data.csv

reddit_data.csv

rss_data.csv

They are designed to be run automatically by main_data_pipeline.py, which orchestrates the entire collection process.

Key Points

Automation-ready: Each script can run individually or as part of the pipeline.

Encoding-safe: UTF-8 is enforced to avoid text issues.

Disaster focus: Queries are focused on disaster-related terms.

Deduplication & standardization: Each script ensures no duplicate entries are saved.

Now, here’s a file-by-file instruction for this folder:

1️⃣ twitter_data.py

Fetches disaster-related tweets using Twitter API.

Filters tweets by keywords like flood, storm, earthquake, etc.

Saves relevant tweet data (text, timestamp, user, etc.) to data/twitter_data.csv.

2️⃣ newsapi_data.py

Pulls news articles from NewsAPI using disaster-related queries.

Extracts title, description, content, source, timestamp.

Deduplicates articles based on url.

Saves to data/newsapi_data.csv.

3️⃣ reddit_data.py

Collects posts/comments from Reddit relevant to disasters.

Includes text, timestamp, subreddit, upvotes and other metadata.

Exports reddit_data.csv in data/.

4️⃣ rss_data.py

Pulls updates from RSS feeds of global disaster and climate news.

Captures title, summary, link, published date.

Outputs rss_data.csv in data/.
