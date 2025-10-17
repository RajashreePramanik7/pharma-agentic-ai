# agents/trials_agent.py
import json, os

class TrialsAgent:
    def __init__(self):
        file_path = os.path.join(os.path.dirname(__file__), "../data/trials_data.json")
        with open(file_path) as f:
            self.data = json.load(f)

    def get_trial_info(self, molecule):
        return self.data.get(molecule, {"active_trials": [], "phase_distribution": {}, "sponsors": []})
