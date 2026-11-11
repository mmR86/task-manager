from fastapi import FastAPI

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