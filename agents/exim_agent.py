# agents/exim_agent.py
import json, os

class EXIMAgent:
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), "../data/exim_data.json")
        with open(file_path) as f:
            self.data = json.load(f)

    def get_trade_data(self, molecule):
        return self.data.get(molecule, {"imports": 0, "exports": 0, "dependencies": []})
