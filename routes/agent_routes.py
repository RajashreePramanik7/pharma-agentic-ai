from fastapi import APIRouter
from agents.master_agent import run_master_agent

router = APIRouter(prefix="/agent", tags=["Agents"])

@router.get("/analyze")
def analyze_molecule(molecule: str):
    result = run_master_agent(molecule)
    return result
