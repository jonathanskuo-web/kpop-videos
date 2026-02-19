import requests
import json
import os

API_KEY = os.environ["YOUTUBE_API_KEY"]

TABS = {
    "xg": "XG kpop",
    "illit": "ILLIT kpop",
    "straykids": "Stray Kids kpop"
}

def search_youtube(query, max_results=10):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "order": "date",
        "key": API_KEY
    }
    r = requests.get(url, params=params)
    items = r.json().get("items", [])
    
    results = []
    for item in items:
        snippet = item["snippet"]
        video_id = item["id"]["videoId"]
        results.append({
            "title": snippet["title"],
            "description": snippet["description"],
            "thumbnail": snippet["thumbnails"]["high"]["url"],
            "published": snippet["publishedAt"],
            "videoId": video_id,
            "url": f"https://www.youtube.com/watch?v={video_id}",
            "channel": snippet["channelTitle"]
        })
    return results

all_data = {}
for tab, query in TABS.items():
    all_data[tab] = search_youtube(query)

with open("data/videos.json", "w") as f:
    json.dump(all_data, f, indent=2)

print("Done!")
