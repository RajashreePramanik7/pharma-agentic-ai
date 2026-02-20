# iqvia_agents.py
import requests

class IQVIAAgent:
    def fetch_market_data(self):
        try:
            resp = requests.get("http://localhost:7000/market-size", timeout=5)
            return resp.json() if resp.ok else {}
        except Exception:
            return {}

    def get_summary(self, data):
        if not data:
            return "No market data available."
        return (
            f"Therapy area: {data.get('therapy_area','N/A')}, "
            f"Market size: ${data.get('market_size',0)/1e6:.1f}M, "
            f"CAGR: {data.get('cagr',0)}%, "
            f"Competitors: {', '.join(data.get('competitors', []))}"
        )
