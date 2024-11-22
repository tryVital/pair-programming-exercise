from contextlib import contextmanager
import sqlite3
from fastapi import Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncSession, async_sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///app.db"
async_engine = create_async_engine(DATABASE_URL, echo=True)


def get_engine() -> AsyncEngine:
    return async_engine


def get_session(db: AsyncEngine = Depends(get_engine)) -> AsyncSession:
    session_maker: async_sessionmaker[AsyncSession] = async_sessionmaker(async_engine, expire_on_commit=False)
    return session_maker()


async def init_db():
    """Initialize the database and create necessary tables"""
    async with get_session(get_engine()) as session:
        await session.execute(text("""
            CREATE TABLE IF NOT EXISTS ...
        """)
        )
        await session.commit()
