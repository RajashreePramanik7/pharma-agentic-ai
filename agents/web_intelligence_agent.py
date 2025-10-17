# agents/web_intelligence_agent.py
import json, os

class WebAgent:
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), "../data/web_results.json")
        with open(file_path) as f:
            self.data = json.load(f)

    def get_web_insights(self, molecule):
        return self.data.get(molecule, {"guidelines": [], "news": [], "pubs": []})
