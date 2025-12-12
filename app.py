from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi import Response

from config.database import engine, Base
from routes import agent_routes, user_routes, history_routes

app = FastAPI(title="Agentic AI - Pharma Innovation API")

# CORS for frontend (Vite)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Create tables
Base.metadata.create_all(bind=engine)

# Static folder for PDF reports
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.options("/{rest_of_path:path}")
def options_handler(rest_of_path: str):
    return Response(status_code=200)

# Routers
app.include_router(user_routes.router)
app.include_router(agent_routes.router)
app.include_router(history_routes.router)

@app.get("/")
def home():
    return {"message": "Welcome to Agentic AI Pharma API"}
