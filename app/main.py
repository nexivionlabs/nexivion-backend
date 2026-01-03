from fastapi import FastAPI
from app.api.v1 import users

app = FastAPI(title="Nexivion Backend")

app.include_router(users.router)

@app.get("/")
def root():
    return {"status": "Nexivion backend running"}
