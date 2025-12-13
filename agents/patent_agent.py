# patent_agent.py
import requests

USPTO_API = "https://developer.uspto.gov/ibd-api/v1/patent/application"

def search_patents(molecule: str):
    query = {
        "q": f"{molecule}",
        "f": ["patentNumber", "patentTitle", "patentIssueDate"],
        "o": {"per_page": 10}
    }

    res = requests.post(USPTO_API, json=query)
    res.raise_for_status()
    return res.json()
