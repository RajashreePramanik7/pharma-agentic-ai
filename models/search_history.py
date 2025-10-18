from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from config.database import Base

class SearchHistory(Base):
    __tablename__ = "search_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)  # Associate with user
    molecule = Column(String(255), nullable=False)
    searched_at = Column(DateTime(timezone=True), server_default=func.now())
