import tweepy
import pandas as pd
from datetime import datetime
import os
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# Load token safely
try:
    from config import TWITTER_BEARER_TOKEN
    print(f"Token loaded: {TWITTER_BEARER_TOKEN[:5]}...{TWITTER_BEARER_TOKEN[-5:]}")
except ImportError:
    print("Could not import from config.py")
    TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN")
    if TWITTER_BEARER_TOKEN:
        print("Using token from environment variable")
    else:
        print("No token available")

def fetch_twitter_v2_data(limit=10):
    print("Starting Twitter v2 fetch test...")

    if not TWITTER_BEARER_TOKEN:
        print("Bearer token is missing or empty")
        return []

    try:
        client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
        print("Client initialized")

        tweets_data = []
        query = "earthquake lang:en"
        print(f"Querying Twitter for: {query}")

        tweets = client.search_recent_tweets(
            query=query,
            max_results=limit,
            tweet_fields=["created_at", "text", "author_id"]
        )

        if not tweets:
            print("No response from Twitter API")
            return []

        print(f"Response metadata: {tweets.meta if hasattr(tweets, 'meta') else 'No metadata'}")

        if tweets.data:
            for tweet in tweets.data:
                tweets_data.append({
                    "title": "Tweet about disaster",
                    "content": tweet.text,
                    "url": f"https://twitter.com/i/web/status/{tweet.id}",
                    "source": "Twitter (v2)",
                    "timestamp": tweet.created_at.strftime("%Y-%m-%d %H:%M:%S") if tweet.created_at else "Unknown"
                })
            print(f"{len(tweets_data)} tweets fetched successfully.")
        else:
            print("No tweets found for this query.")

    except tweepy.TweepyException as te:
        print(f"Tweepy error: {te}")
        tweets_data = []
    except Exception as e:
        print(f"General error: {e}")
        import traceback
        traceback.print_exc()
        tweets_data = []

    # Save data
    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(ROOT_DIR, "data")
    os.makedirs(DATA_DIR, exist_ok=True)

    if tweets_data:
        df = pd.DataFrame(tweets_data)
        output_path = os.path.join(DATA_DIR, "twitter_data.csv")
        df.to_csv(output_path, index=False, encoding="utf-8")
        print(f"Saved {len(df)} tweets to {output_path}")
    else:
        print("No data to save.")

    return tweets_data


if __name__ == "__main__":
    results = fetch_twitter_v2_data()
    print(f"Final results count: {len(results)}")
