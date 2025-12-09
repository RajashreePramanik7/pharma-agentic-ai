# routes/user_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from config.database import get_db
from models.user_model import User
from utils.auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

router = APIRouter()


# --------------------------------
# Request Schemas
# --------------------------------
class SignupSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


# --------------------------------
# SIGNUP — Create New User
# --------------------------------
@router.post("/api/users/register")
def register(data: SignupSchema, db: Session = Depends(get_db)):

    # Check if user already exists
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered.")

    # Create new user
    user = User(
        name=data.name,
        email=data.email,
        hashed_password=hash_password(data.password),
        provider="email"
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return {"message": "User registered successfully."}


# --------------------------------
# LOGIN — Return JWT Token
# --------------------------------
@router.post("/api/users/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):

    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password.")

    if user.provider != "email":
        raise HTTPException(
            status_code=400,
            detail="This account requires a different login method."
        )

    if not verify_password(data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password.")

    token = create_access_token({"sub": user.email})

    return {
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "provider": user.provider,
            "created_at": user.created_at,
        },
    }


# --------------------------------
# GET CURRENT USER PROFILE
# --------------------------------
@router.get("/api/users/me")
def get_my_profile(
    email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(User.email == email).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "provider": user.provider,
        "created_at": user.created_at,
    }
@router.post("/api/users/register")
def register(data: SignupSchema, db: Session = Depends(get_db)):
    print("Signup request received:", data)
