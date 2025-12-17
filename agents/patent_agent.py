# patent_agents.py
import requests

class PatentAgent:
    def fetch_patent_status(self):
        try:
            resp = requests.get("http://localhost:7002/patent-status", timeout=5)
            return resp.json() if resp.ok else {}
        except Exception:
            return {}
