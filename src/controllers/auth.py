from datetime import datetime, timedelta

from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select, Result
from sqlalchemy.ext.asyncio import AsyncSession
from jose import jwt, ExpiredSignatureError, JWTError
from decouple import config

from src.base.database import get_session_maker
from src.models.database import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def encode_token(sub: int) -> str:
	return jwt.encode(
		{"sub": str(sub), "exp": datetime.now() + timedelta(weeks=30), "iat": datetime.now()},
		config("JWT_TOKEN_SECRET")
	)


def decode_token(token: str) -> dict:
	return jwt.decode(token, config("JWT_TOKEN_SECRET"))


def check_token(token: str) -> int:
	try:
		token_data = decode_token(token)
		return int(token_data["sub"])
	except ExpiredSignatureError:
		raise ValueError("Token expired")
	except JWTError:
		raise ValueError("Invalid token")


def validate_user_token(token: str = Depends(oauth2_scheme)):
	# TODO: OPT: Add check for valid user in database by 'sub' field in token
	try:
		check_token(token)
	except ValueError as e:
		raise HTTPException(status_code=401, detail=str(e))


async def login(*, username: str, password: str) -> str:
	async with get_session_maker()() as session:
		session: AsyncSession

		db_result: Result = await session.execute(select(User).where(User.login == username, User.password == password))
		user: User = db_result.scalars().first()
		if not user:
			raise HTTPException(401, "Invalid username or password")
		return encode_token(user.id)
