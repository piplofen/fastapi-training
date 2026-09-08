from sqlalchemy.ext.asyncio import  (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncIterator
from config import settings

class Base(DeclarativeBase):
    pass

engine = create_async_engine(
    settings.database_url,
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True,
    echo=True,
)

SessionFactory = async_sessionmaker(
    engine,
    expire_on_commit=False,
    autoflush=False,
)

async def get_session() -> AsyncIterator[AsyncSession]:
    async with SessionFactory() as session:
        yield session