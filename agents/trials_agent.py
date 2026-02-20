import requests
import pandas as pd

class ClinicalTrialsAgent:
    BASE_URL = "http://localhost:7003/clinical-trials"

    def fetch_trials(self, indication=None, moa=None, country=None):
        params = {}
        if indication:
            params["indication"] = indication
        if moa:
            params["moa"] = moa
        if country:
            params["country"] = country
        try:
            resp = requests.get(self.BASE_URL, params=params, timeout=5)
            return resp.json().get("trials", []) if resp.ok else []
        except Exception:
            return []

    def to_dataframe(self, trials):
        if not trials:
            return pd.DataFrame(columns=["nct_id", "phase", "status", "sponsor", "country"])
        return pd.DataFrame(trials)[["nct_id", "phase", "status", "sponsor", "country"]]

    def get_summary(self, trials):
        if not trials:
            return "No clinical trials found for the given criteria."
        df = self.to_dataframe(trials)
        phase_counts = df["phase"].value_counts().to_dict()
        sponsor_counts = df["sponsor"].value_counts().to_dict()
        return (
            f"Found {len(trials)} trials. "
            f"Phase distribution: {phase_counts}. "
            f"Top sponsors: {sponsor_counts}."
        )
