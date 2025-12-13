# trials_agent.py
import requests

BASE_URL = "https://clinicaltrials.gov/api/query/study_fields"

def get_trials(molecule: str):
    params = {
        "expr": molecule,
        "fields": "NCTId,Condition,Phase,OverallStatus,SponsorName",
        "min_rnk": 1,
        "max_rnk": 20,
        "fmt": "json"
    }

    res = requests.get(BASE_URL, params=params, timeout=20)
    res.raise_for_status()

    return res.json()["StudyFieldsResponse"]["StudyFields"]
