from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.model.user import Base
from app.config.db_config import engine
from app.controller.auth_controller import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Shutdown (gerekirse burada cleanup yapılır)


app = FastAPI(
    title="Chat App",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(auth_router)
