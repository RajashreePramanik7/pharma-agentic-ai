from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.search_history import SearchHistory
from config.database import SessionLocal
from pydantic import BaseModel
from typing import List
from datetime import datetime

router = APIRouter(prefix="/api/history")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Request schema
class SaveSearchRequest(BaseModel):
    user_id: int
    molecule: str

# Response schema
class SearchHistoryResponse(BaseModel):
    id: int
    user_id: int
    molecule: str
    searched_at: datetime

    class Config:
        orm_mode = True

# Save a new search
@router.post("/", response_model=SearchHistoryResponse)
def save_search(req: SaveSearchRequest, db: Session = Depends(get_db)):
    new_search = SearchHistory(user_id=req.user_id, molecule=req.molecule)
    db.add(new_search)
    db.commit()
    db.refresh(new_search)
    return new_search

# Get search history for a user, sorted by date ascending
@router.get("/{user_id}", response_model=List[SearchHistoryResponse])
def get_history(user_id: int, db: Session = Depends(get_db)):
    history = db.query(SearchHistory).filter(SearchHistory.user_id == user_id)\
        .order_by(SearchHistory.searched_at.asc()).all()
    return history
