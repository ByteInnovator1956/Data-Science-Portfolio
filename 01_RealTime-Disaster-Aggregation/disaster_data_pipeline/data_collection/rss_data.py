import feedparser
import pandas as pd
from datetime import datetime
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def fetch_rss_data():
    print("Fetching data from RSS feeds...")

    feeds = [
        "https://www.emsc-csem.org/service/rss/rss.php",
        "https://www.sciencedaily.com/rss/earth_climate/natural_disasters.xml",
        "https://www.nasa.gov/rss/dyn/earth.rss",
        "https://reliefweb.int/updates/rss.xml"
    ]

    articles = []

    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        print(f"Parsed {len(feed.entries)} entries from {feed_url}")

        for entry in feed.entries:
            articles.append({
                "source": "RSS",
                "title": entry.get("title", ""),
                "summary": entry.get("summary", ""),
                "link": entry.get("link", ""),
                "published": entry.get("published", datetime.now())
            })

    df = pd.DataFrame(articles)
    df.to_csv("data/rss_data.csv", index=False, encoding="utf-8")
    print(f"Saved {len(df)} entries to data/rss_data.csv")

if __name__ == "__main__":
    fetch_rss_data()
