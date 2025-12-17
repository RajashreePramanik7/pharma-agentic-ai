from fastapi import APIRouter, HTTPException
from agents.master_agent import MasterAgent

router = APIRouter(prefix="/api/agent", tags=["Agentic AI"])

@router.post("/query")
def run_query(payload: dict):
    try:
        agent = MasterAgent()

        return agent.analyze_portfolio(
            query=payload.get("query"),
            product=payload.get("molecule", "salbutamol"),
            therapy=payload.get("therapy", "respiratory"),
            country=payload.get("country", "India"),
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))