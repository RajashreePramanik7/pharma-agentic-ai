# agents/exim_agent.py
import requests
import os

EXIM_API_KEY = os.getenv("EXIM_API_KEY")

def fetch_exim_trends(molecule: str):
    response = requests.get(
        "https://api.eximdata.com/v1/trade",
        params={"query": molecule},
        headers={"Authorization": f"Bearer {EXIM_API_KEY}"}
    )

    data = response.json()

    return {
        "molecule": molecule,
        "top_importers": data["top_importing_countries"],
        "top_exporters": data["top_exporting_countries"],
        "volume_trend": data["trend"],
        "import_dependency": data["dependency_score"]
    }
