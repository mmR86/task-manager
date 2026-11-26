import app.models
from fastapi import FastAPI

from app.api.v1.endpoints.auth import router as auth_router

app = FastAPI(
    title="Task Manager API",
    description="A task management API built with FastAPI and PostgreSQL.",
    version="1.0.0",
)

app.include_router(auth_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Task Manager API is running!"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}