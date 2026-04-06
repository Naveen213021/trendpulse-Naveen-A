# Task 1 - TrendPulse Data Collection
# Fetch trending stories from the HackerNews API and categorize them

import requests
import json
import os
import time
from datetime import datetime
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"
headers = {"User-Agent": "TrendPulse/1.0"}

categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

collected_stories = []

category_count = {cat: 0 for cat in categories}

def categorize_title(title):
    title_lower = title.lower()

    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category

    return None


# Step 1: Fetch top story IDs
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:500]  # Only first 500
except Exception as e:
    print("Failed to fetch top stories:", e)
    exit()
collected_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Step 2: Fetch each story and categorize
for story_id in story_ids:

    if all(count >= 50 for count in category_count.values()):
        break

    try:
        story_response = requests.get(ITEM_URL.format(story_id), headers=headers)
        story = story_response.json()

        if not story or "title" not in story:
            continue

        title = story.get("title", "")
        category = categorize_title(title)

        if category is None:
            continue
        if category_count[category] >= 50:
            continue
        story_data = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": collected_time
        }

        collected_stories.append(story_data)
        category_count[category] += 1

    except Exception as e:
        print(f"Failed to fetch story {story_id}: {e}")
        continue
for _ in categories:
    time.sleep(2)

# Step 3: Save results to JSON

os.makedirs("data", exist_ok=True)

date_str = datetime.now().strftime("%Y%m%d")
filename = f"data/trends_{date_str}.json"

with open(filename, "w", encoding="utf-8") as f:
    json.dump(collected_stories, f, indent=4)

print(f"Collected {len(collected_stories)} stories. Saved to {filename}")
