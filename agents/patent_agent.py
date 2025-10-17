# agents/patent_agent.py
import json, os

class PatentAgent:
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), "../data/patents_data.json")
        with open(file_path) as f:
            self.data = json.load(f)

    def get_patent_info(self, molecule):
        return self.data.get(molecule, {"active_patents": [], "expiry": [], "freetooperate": True})
