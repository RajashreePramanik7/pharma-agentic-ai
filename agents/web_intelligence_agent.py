import requests
import pandas as pd

class WebIntelligenceAgent:
    BASE_URL = "http://localhost:7005/web-search"

    def search(self, query: str):
        try:
            resp = requests.get(self.BASE_URL, params={"q": query}, timeout=5)
            return resp.json().get("results", []) if resp.ok else []
        except Exception:
            return []

    def to_dataframe(self, results):
        if not results:
            return pd.DataFrame(columns=["title", "url", "snippet"])
        return pd.DataFrame(results)[["title", "url", "snippet"]]

    def get_summary(self, results):
        if not results:
            return "No web signals found."
        bullets = []
        for r in results[:3]:
            bullets.append(f"- {r['title']} ({r['url']})")
        return "Key external references:\n" + "\n".join(bullets)
