from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from src.database.models import Base, User
from src.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER


#DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'

engine = create_async_engine(url=DATABASE_URL)

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)


async def creating_tables():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
