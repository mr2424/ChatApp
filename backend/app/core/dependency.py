from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.db_config import get_db
from app.repository.user_repository import UserRepository
from app.service.user_service import UserService


def get_user_repository(db: AsyncSession = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_user_service(user_repo: UserRepository = Depends(get_user_repository)) -> UserService:
    return UserService(user_repo)
