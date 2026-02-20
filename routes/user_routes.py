# routes/user_routes.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr

from config.database import get_db
from models.user_model import User
from utils.auth import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


# -----------------------------
# Pydantic Schemas
# -----------------------------
class SignupSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


# -----------------------------
# SIGNUP
# -----------------------------
@router.post("/api/users/register")
def register_user(body: SignupSchema, db: Session = Depends(get_db)):
    # Check if email exists
    user = db.query(User).filter(User.email == body.email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        name=body.name,
        email=body.email,
        password=hash_password(body.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


# -----------------------------
# LOGIN
# -----------------------------
@router.post("/api/users/login")
def login_user(body: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == body.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not verify_password(body.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    token = create_access_token({"user_id": user.id})

    return {
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
        }
    }
