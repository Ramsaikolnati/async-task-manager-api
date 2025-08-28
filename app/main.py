# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import users, task_routes, auth  # <-- match your actual files

app = FastAPI(
    title="Async Task Manager API",
    version="1.0.0",
    description="A simple async task manager with FastAPI + SQLAlchemy + JWT",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change in prod
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(task_routes.router)


@app.get("/")
async def root():
    return {"message": "Async Task Manager API is running 🚀"}