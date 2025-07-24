from sqlalchemy import Column, Integer, String, DateTime

from src.base.database import Base


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, autoincrement=True)
	login = Column(String, nullable=False)
	password = Column(String, nullable=False)


class Task(Base):
	__tablename__ = "tasks"

	id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String, nullable=False)
	description = Column(String, nullable=False)
	status = Column(String, nullable=False)
	time_created = Column(DateTime, nullable=False, server_default="CURRENT_TIMESTAMP")
