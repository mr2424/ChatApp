from pydantic import BaseModel, EmailStr
from datetime import datetime

class SignupRequest(BaseModel):
    username: str
    password: str
    email: EmailStr | None = None
    first_name: str
    last_name: str

class LoginRequest(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    username: str
    email: EmailStr | None = None
    first_name: str
    last_name: str
    created_at: datetime

class AuthToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
