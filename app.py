from fastapi import FastAPI
from routes import agent_routes

app = FastAPI(title="Agentic AI - Pharma Innovation API")

# include your route file
app.include_router(agent_routes.router)

@app.get("/")
def home():
    return {"message": "Welcome to Agentic AI Pharma API"}
