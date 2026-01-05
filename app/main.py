from fastapi import FastAPI
from app.routers import users

app = FastAPI(title="Nexivion Backend")

app.include_router(users.router)

@app.get("/")
def root():
    return {"status": "ok"}
