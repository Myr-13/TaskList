from datetime import datetime, timedelta

from fastapi import HTTPException
from jose import jwt, ExpiredSignatureError, JWTError
from sqlalchemy import select, Result

from src.base.database import get_session_maker
from src.models.database import User


def encode_token(sub: int) -> str:
	return jwt.encode(
		{"sub": sub, "exp": datetime.now() + timedelta(weeks=30), "iat": datetime.now()},
		""
	)


def decode_token(token: str) -> dict:
	return jwt.decode(token, "")


def check_token(token: str) -> int:
	try:
		token_data = decode_token(token)
		return token_data["sub"]
	except ExpiredSignatureError:
		raise ValueError("Token expired")
	except JWTError:
		raise ValueError("Invalid token")


async def login(*, username: str, password: str) -> str:
	async with get_session_maker()() as session:
		db_result: Result = await session.execute(select(User).where(User.login == username, User.password == password))
		user: User = db_result.scalars().first()
		if not user:
			raise HTTPException(401, "Invalid username or password")
		return encode_token(user.id)
