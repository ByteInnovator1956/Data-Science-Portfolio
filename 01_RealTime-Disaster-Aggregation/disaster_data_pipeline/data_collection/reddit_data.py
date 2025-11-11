import praw
import pandas as pd
from datetime import datetime
import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Import Reddit API credentials from config.py
try:
    from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
    print("Reddit credentials loaded from config.py")
except ImportError:
    print("Could not import from config.py, checking environment variables...")
    REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
    REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
    REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT", "disaster_fetcher")

def fetch_reddit_data(limit=20):
    print("Fetching data from Reddit...")

    # Initialize Reddit client
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )
        print("Reddit client initialized successfully")
    except Exception as e:
        print(f"Error initializing Reddit client: {e}")
        return []

    keywords = [
        "earthquake", "flood", "wildfire", "tsunami", "cyclone",
        "landslide", "volcano", "storm", "natural disaster"
    ]
    posts_data = []

    for keyword in keywords:
        print(f"Searching for: {keyword}")
        try:
            for submission in reddit.subreddit("all").search(keyword, limit=limit):
                posts_data.append({
                    "source": "Reddit",
                    "keyword": keyword,
                    "title": submission.title,
                    "text": submission.selftext,
                    "url": submission.url,
                    "created_utc": datetime.utcfromtimestamp(submission.created_utc),
                    "score": submission.score
                })
        except Exception as e:
            print(f"Error fetching for keyword '{keyword}': {e}")

    # Save results
    if posts_data:
        df = pd.DataFrame(posts_data)
        os.makedirs("data", exist_ok=True)
        df.to_csv("data/reddit_data.csv", index=False, encoding="utf-8")
        print(f"Saved {len(df)} posts to data/reddit_data.csv")
    else:
        print("No Reddit posts fetched.")

    return posts_data

if __name__ == "__main__":
    fetch_reddit_data(limit=10)
