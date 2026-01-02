from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# ===== SCHEMA =====
class User(BaseModel):
    id: int
    name: str

# ===== SAHTE VERİ =====
fake_users_db: List[User] = [
    User(id=1, name="Ali"),
    User(id=2, name="Veli"),
]

# ===== ENDPOINTLER =====
@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/users", response_model=List[User])
def get_users():
    return fake_users_db

@app.post("/users", response_model=User)
def create_user(user: User):
    fake_users_db.append(user)
    return user

