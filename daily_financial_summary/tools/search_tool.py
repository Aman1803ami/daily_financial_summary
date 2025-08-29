import os, requests, datetime
from dateutil import parser as dateparser

SEARCH_API_KEY = os.getenv("SEARCH_API_KEY", "PUT_KEY_HERE")
SEARCH_API_ENDPOINT = os.getenv("SEARCH_API_ENDPOINT", "https://api.serper.dev/search")

def search_tool(query="US stock market news", last_minutes=60, limit=8):
    cutoff = datetime.datetime.utcnow() - datetime.timedelta(minutes=last_minutes)
    headers = {"X-API-KEY": SEARCH_API_KEY, "Content-Type": "application/json"}
    payload = {"q": query, "num": limit}

    r = requests.post(SEARCH_API_ENDPOINT, headers=headers, json=payload, timeout=15)
    r.raise_for_status()
    data = r.json()

    results = []
    for it in data.get("organic", []):
        title, link, snippet = it.get("title"), it.get("link"), it.get("snippet")
        published = it.get("date")
        published_dt = None
        try:
            published_dt = dateparser.parse(published) if published else None
        except:
            pass
        if published_dt and published_dt < cutoff:
            continue
        results.append({"title": title, "link": link, "snippet": snippet, "published": published})
    return results