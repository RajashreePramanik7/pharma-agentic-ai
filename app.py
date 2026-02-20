# app.py

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from config.database import engine, Base
from routes import agent_routes, user_routes, history_routes

app = FastAPI(title="Agentic AI - Pharma Innovation API")

# -----------------------------
# CORS SETTINGS (WORKING)
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# DATABASE
# -----------------------------
Base.metadata.create_all(bind=engine)

# -----------------------------
# STATIC FOLDER
# -----------------------------
app.mount("/static", StaticFiles(directory="static"), name="static")

# -----------------------------
# ROUTERS
# -----------------------------
app.include_router(user_routes.router)
app.include_router(agent_routes.router)
app.include_router(history_routes.router)

@app.get("/")
def home():
    return {"message": "Welcome to Agentic AI Pharma API"}
