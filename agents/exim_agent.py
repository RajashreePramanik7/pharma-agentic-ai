# exim_agents.py
import requests

class EXIMAgent:
    def fetch_trade_data(self):
        try:
            resp = requests.get("http://localhost:7001/trade-volume", timeout=5)
            return resp.json() if resp.ok else {}
        except Exception:
            return {}

    def get_bullets(self, data):
        if not data:
            return ["No trade data available."]
        bullets = [
            f"API: {data.get('api_name','N/A')}",
            f"Export volume: {data.get('export_volume_kg',0)} kg",
            f"Import dependency: {data.get('import_dependency','N/A')}",
            f"Key countries: {', '.join(data.get('countries', []))}",
        ]
        return bullets
