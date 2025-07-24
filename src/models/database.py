from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, BLOB

from src.base.database import Base


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True)
	login = Column(String(64), nullable=False)
	password = Column(String(32), nullable=False)
