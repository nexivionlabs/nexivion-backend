from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.user import User, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

fake_users_db: List[User] = []

@router.get("/", response_model=List[User])
def get_users():
    return fake_users_db


@router.post("/", response_model=User)
def create_user(user: UserCreate):
    # duplicate name engeli
    for existing in fake_users_db:
        if existing.name.lower() == user.name.lower():
            raise HTTPException(
                status_code=400,
                detail="Bu isimde bir kullanıcı zaten var"
            )

    new_id = len(fake_users_db) + 1
    new_user = User(id=new_id, name=user.name)
    fake_users_db.append(new_user)
    return new_user

@router.get("/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in fake_users_db:
        if user.id == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="Kullanıcı bulunamadı"
    )
