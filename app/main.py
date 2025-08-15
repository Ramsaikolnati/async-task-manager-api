from fastapi import FastAPI

app=FastAPI(title="Async Task Manager API")

@app.get("/")
def root():
    return {"message":"Welcome to Async Task Manager API"}