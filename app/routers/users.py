from fastapi import APIRouter, HTTPException
from typing import List

from app.schemas.user import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

fake_users_db: List[User] = []
current_id = 1


@router.get("/", response_model=List[User])
def get_users():
    return fake_users_db


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    global current_id

    new_user = User(
        id=current_id,
        name=user.name
    )

    fake_users_db.append(new_user)
    current_id += 1

    return new_user


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in fake_users_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")
