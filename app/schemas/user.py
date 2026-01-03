from pydantic import BaseModel

class UserCreate(BaseModel):
    message: str  # kullanıcının ihtiyacını anlattığı metin

class UserResponse(BaseModel):
    decision: str
    suggested_service: str
