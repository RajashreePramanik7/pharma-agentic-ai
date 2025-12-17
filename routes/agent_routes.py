from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from agents.master_agent import MasterAgent
from pathlib import Path

router = APIRouter(prefix="/api/agent", tags=["Agentic AI"])

PDF_DIR = Path("generated_pdfs")

@router.post("/query")
def run_query(payload: dict):
    agent = MasterAgent()
    return agent.analyze_portfolio(
        query=payload.get("query"),
        product=payload.get("molecule"),
        therapy=payload.get("therapy"),
        country=payload.get("country"),
        sources=payload.get("sources", []),
    )

@router.get("/download/{filename}")
def download_pdf(filename: str):
    pdf_path = PDF_DIR / filename
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="PDF not found")
    return FileResponse(pdf_path, media_type="application/pdf", filename=filename)