import logging
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from httpcore import AsyncConnectionPool
from sqlalchemy.pool import AsyncAdaptedQueuePool
from sqlalchemy.exc import OperationalError, SQLAlchemyError
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.infrastructure.models.database import Base
from app.infrastructure.database.repos import Repositories
from config.config import settings

logger = logging.getLogger("Database")

async_engine = create_async_engine(
    url=settings.db.url_asyncpg,
    echo=True,
    poolclass=AsyncAdaptedQueuePool,
    pool_size=10,
    max_overflow=10
)

async_session = async_sessionmaker(
    bind=async_engine, expire_on_commit=False, autoflush=False
)


@asynccontextmanager
async def get_repo() -> AsyncGenerator[Repositories, None]:
    """Return db repos with active session"""
    async with async_session() as s:
        logger.debug("session was create")
        yield Repositories.get_repo(s)


async def crete_tables() -> None:
    """Creating tables and check db connection"""
    try:
        async with async_engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            logger.debug("Database connected and tables created successfully")

    except OperationalError as e:
        logger.critical(f"Database connection failed: {e}")
        raise RuntimeError("Database connection failed") from e

    except SQLAlchemyError as e:
        logger.critical(f"SQLAlchemy error while creating tables: {e}")
        raise RuntimeError("Error while creating database schema") from e

    except Exception as e:
        logger.exception("Unexpected error during database initialization")
        raise RuntimeError("Unexpected database initialization error") from e
