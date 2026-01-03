from fastapi import APIRouter
from app.schemas.user import UserCreate, UserResponse
from app.services.ai_agent import analyze_user_request

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate):
    decision = analyze_user_request(user.message)

    return {
        "decision": decision,
        "suggested_service": "Web Development"
    }
