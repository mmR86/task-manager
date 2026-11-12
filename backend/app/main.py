from fastapi import FastAPI
from sqlalchemy import text

from app.db.session import engine

app = FastAPI(
    title="Task Manager API",
    description="A full-stack task management application",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"message": "Task Manager API is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/health/db")
def database_health_check():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))

    return {
        "database": "connected",
        "test_query": result.scalar(),
    }