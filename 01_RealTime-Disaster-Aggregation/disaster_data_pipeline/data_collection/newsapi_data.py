import requests
import pandas as pd
import os
from datetime import datetime
from config import NEWS_API_KEY
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Broad disaster-related search queries
DISASTER_QUERIES = [
    "natural disaster",
    "natural calamity",
    "extreme weather",
    "severe storm",
    "disaster news",
    "catastrophic event"
]

def fetch_newsapi_multiquery(limit_per_query=20):
    print("Starting multi-query NewsAPI fetch...")

    all_articles = []
    base_url = "https://newsapi.org/v2/everything"

    for query in DISASTER_QUERIES:
        print(f"\nFetching news for: '{query}'...")
        params = {
            "q": query,
            "language": "en",
            "pageSize": limit_per_query,
            "sortBy": "publishedAt",
            "apiKey": NEWS_API_KEY
        }

        try:
            response = requests.get(base_url, params=params)
            data = response.json()

            if response.status_code == 200 and data.get("articles"):
                for article in data["articles"]:
                    all_articles.append({
                        "title": article.get("title"),
                        "description": article.get("description"),
                        "content": article.get("content"),
                        "url": article.get("url"),
                        "source": article["source"].get("name"),
                        "query": query,
                        "timestamp": article.get("publishedAt")
                    })
                print(f"{len(data['articles'])} articles fetched for '{query}'")
            else:
                print(f"No data found for '{query}' (status {response.status_code})")

        except Exception as e:
            print(f"Error fetching '{query}': {e}")

    # Deduplicate & save
    if all_articles:
        df = pd.DataFrame(all_articles)
        df.drop_duplicates(subset=["url"], inplace=True)
        df.reset_index(drop=True, inplace=True)

        ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        DATA_DIR = os.path.join(ROOT_DIR, "data")
        os.makedirs(DATA_DIR, exist_ok=True)

        output_path = os.path.join(DATA_DIR, "newsapi_data.csv")
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"\nSaved {len(df)} unique articles to {output_path}")
    else:
        print("\nNo data to save.")
        df = pd.DataFrame()

    return df


if __name__ == "__main__":
    df = fetch_newsapi_multiquery(limit_per_query=20)
    print(f"\nTotal unique records: {len(df)}")
