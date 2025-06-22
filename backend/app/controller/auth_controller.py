from fastapi import APIRouter, Depends
from app.dto.user_dto import SignupRequest, LoginRequest, UserResponse, AuthToken
from app.service.user_service import UserService
from app.core.dependency import get_user_service

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup", response_model=UserResponse)
async def signup(
        request: SignupRequest,
        service: UserService = Depends(get_user_service)
):
    return await service.signup(request)


@router.post("/login", response_model=AuthToken)
async def login(
        request: LoginRequest,
        service: UserService = Depends(get_user_service)
):
    return await service.login(request)
