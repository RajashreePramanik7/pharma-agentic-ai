# routes/user_routes.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from config.database import get_db
from models.user_model import User
from google.oauth2 import id_token
from google.auth.transport import requests as grequests

router = APIRouter()

# Pydantic model to read JSON body
class TokenSchema(BaseModel):
    token: str

@router.post("/api/auth/google")
def google_login(body: TokenSchema, db: Session = Depends(get_db)):
    token = body.token
    try:
        # Verify the Google token
        info = id_token.verify_oauth2_token(token, grequests.Request())
        email = info.get("email")
        name = info.get("name")

        if not email:
            raise HTTPException(status_code=400, detail="Google login failed: email missing")

        # Check if user exists
        user = db.query(User).filter(User.email == email).first()

        if not user:
            # Create new user
            user = User(name=name, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)

        return {"message": "Login successful", "user": {"name": name, "email": email}}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
