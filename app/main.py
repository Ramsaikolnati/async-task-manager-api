from fastapi import FastAPI
from app.api import task_routes
from app.db import Base, engine


app=FastAPI(title="Async Task Manager API")

# Create tables at startup
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Register routes
app.include_router(task_routes.router)

@app.get("/")
def root():
    return {"message":"Welcome to Async Task Manager API"}