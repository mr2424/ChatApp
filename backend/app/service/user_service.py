from app.repository.user_repository import UserRepository
from app.dto.user_dto import SignupRequest, LoginRequest, UserResponse, AuthToken
from app.utils.password_hasher import verify_password
from app.utils.jwt_handler import create_access_token
from fastapi import HTTPException

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def signup(self, request: SignupRequest) -> UserResponse:
        existing_user = await self.repo.get_by_username(request.username)
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        user = await self.repo.create_user_from_request(request)
        return UserResponse(
            username=user.username,
            email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            created_at=user.created_at
        )

    async def login(self, request: LoginRequest) -> AuthToken:
        user = await self.repo.get_by_username(request.username)
        if not user or not verify_password(request.password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        token = create_access_token({"sub": user.username})
        return AuthToken(access_token=token)
