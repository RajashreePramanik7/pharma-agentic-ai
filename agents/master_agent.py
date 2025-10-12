def run_master_agent(query):
    # For now, mock a simple response
    summary = f"Running analysis for molecule: {query}"
    insights = {
        "market": "Moderate growth (6%) in respiratory drugs",
        "patents": "Low saturation, opportunities in inhalable forms",
        "clinical_trials": 12,
    }

    return {
        "query": query,
        "summary": summary,
        "insights": insights,
        "status": "success"
    }
