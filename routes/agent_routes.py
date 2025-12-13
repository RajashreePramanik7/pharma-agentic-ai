# routes/agent_routes.py
from fastapi import APIRouter
from agents.master_agent import run_master_agent

router = APIRouter()

@router.post("/api/agent/query")
def run_query(payload: dict):
    query = payload["query"]
    molecule = payload["molecule"]

    result = run_master_agent(query, molecule)
    return result
