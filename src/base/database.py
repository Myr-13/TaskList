import logging

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

Base = declarative_base()
_session_maker: async_sessionmaker = ...


async def initialize_db(user: str, password: str, ip: str, database_name: str) -> None:
	global _session_maker

	logging.info("Initializing database")

	url: str = f"postgresql+asyncpg://{user}:{password}@{ip}/{database_name}"
	engine = create_async_engine(url)
	_session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, autocommit=False, autoflush=False)

	logging.info("Connected to database")


def get_session_maker() -> async_sessionmaker:
	return _session_maker
