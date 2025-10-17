# routes/agents_routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from agents.master_agent import MasterAgent

router = APIRouter()
master_agent = MasterAgent()

# Request schema
class MoleculeRequest(BaseModel):
    molecule: str
    sources: list[str] = ["market", "patent", "trials", "web", "trade"]

@router.post("/api/molecule")
def analyze_molecule(request: MoleculeRequest):
    try:
        results = master_agent.analyze_molecule(request.molecule, request.sources)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
