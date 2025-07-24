import pytest_asyncio

from src.base.database import initialize_test_db


@pytest_asyncio.fixture
async def database():
	await initialize_test_db()
