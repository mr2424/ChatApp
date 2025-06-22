from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.model.user import User
from app.dto.user_dto import SignupRequest
from app.utils.password_hasher import hash_password

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_username(self, username: str) -> User | None:
        result = await self.session.execute(select(User).where(User.username == username))
        return result.scalars().first()

    async def create_user_from_request(self, request: SignupRequest) -> User:
        user = User(
            username=request.username,
            email=request.email,
            first_name=request.first_name,
            last_name=request.last_name,
            hashed_password=hash_password(request.password)
        )
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
