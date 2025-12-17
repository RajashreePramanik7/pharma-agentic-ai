import requests
import pandas as pd

class InternalKnowledgeAgent:
    BASE_URL = "http://localhost:7004/internal-search"

    def search(self, query: str):
        try:
            resp = requests.get(self.BASE_URL, params={"q": query}, timeout=5)
            return resp.json().get("documents", []) if resp.ok else []
        except Exception:
            return []

    def to_dataframe(self, docs):
        if not docs:
            return pd.DataFrame(columns=["id", "title", "tags", "summary"])
        return pd.DataFrame(docs)[["id", "title", "tags", "summary"]]

    def get_summary(self, docs):
        if not docs:
            return "No internal insights found for this topic."
        top_titles = [d["title"] for d in docs[:3]]
        return (
            f"Found {len(docs)} internal documents. "
            f"Key decks include: {', '.join(top_titles)}."
        )
