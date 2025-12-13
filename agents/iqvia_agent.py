# iqvia_agent.py
import requests
import os

IQVIA_API_KEY = os.getenv("IQVIA_API_KEY")
IQVIA_BASE_URL = "https://api.iqvia.com/v1"

def get_market_data(molecule: str):
    headers = {
        "Authorization": f"Bearer {IQVIA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "molecule": molecule,
        "region": "India"
    }

    response = requests.post(
        f"{IQVIA_BASE_URL}/market/insights",
        json=payload,
        headers=headers,
        timeout=30
    )

    response.raise_for_status()
    return response.json()
