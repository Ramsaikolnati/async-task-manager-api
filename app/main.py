from fastapi import FastAPI
from app.api import task_routes, auth, users
from app.db import Base, engine

app = FastAPI(title="Async Task Manager API")

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Register routes
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(task_routes.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Async Task Manager API"}
