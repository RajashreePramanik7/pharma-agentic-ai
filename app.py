from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import agent_routes, user_routes
from config.database import engine, Base

app = FastAPI(title="Agentic AI - Pharma Innovation API")

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(agent_routes.router)  # <--- important
app.include_router(user_routes.router)

@app.get("/")
def home():
    return {"message": "Welcome to Agentic AI Pharma API"}
