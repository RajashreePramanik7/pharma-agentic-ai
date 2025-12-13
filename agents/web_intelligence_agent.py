import requests
import os

SERP_API_KEY = os.getenv("SERP_API_KEY")

def web_search(query: str):
    res = requests.get(
        "https://serpapi.com/search",
        params={
            "q": query,
            "api_key": SERP_API_KEY,
            "engine": "google"
        }
    )

    results = res.json()["organic_results"]

    sources = [
        {"title": r["title"], "url": r["link"]}
        for r in results[:5]
    ]

    return {
        "summary": "Key findings extracted from recent web sources.",
        "sources": sources
    }
