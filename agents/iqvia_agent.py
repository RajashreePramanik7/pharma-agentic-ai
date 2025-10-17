# agents/iqvia_agent.py
import json
import os

class IQVIAAgent:
    def __init__(self):
        # Load mock data
        file_path = os.path.join(os.path.dirname(__file__), "../data/iqvia_data.json")
        with open(file_path) as f:
            self.data = json.load(f)

    def get_market_data(self, molecule):
        # Return mock data filtered by molecule
        return self.data.get(molecule, {"market_size": 0, "growth": 0, "competitors": []})
