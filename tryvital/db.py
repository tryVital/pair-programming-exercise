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


async def read_query(query: str) -> list[dict]:
    async with get_session(get_engine()) as db:
        result = await db.execute(text(query))
        return [dict(row) for row in result.mappings().all()]


async def write_query(query: str) -> None:
    async with get_session(get_engine()) as db:
        await db.execute(text(query))
        await db.commit()


async def init_db():
    """Initialize the database and create necessary tables"""

    await write_query(
        """
        CREATE TABLE IF NOT EXISTS ...
        """
    )
