from enum import StrEnum
from pydantic import BaseModel

from src.models.objects import TaskObject


# Auth
class LoginRequest(BaseModel):
	username: str
	password: str


class LoginResponse(BaseModel):
	token: str


# Task list
class TaskStatus(StrEnum):
	PENDING = "pending"
	IN_PROGRESS = "in_progress"
	DONE = "done"


class TaskField(StrEnum):
	TITLE = "title"
	DESCRIPTION = "description"
	STATUS = "status"


class TaskCreateRequest(BaseModel):
	title: str
	description: str
	status: TaskStatus


class TaskListResponse(BaseModel):
	tasks: list[TaskObject]


class TaskEditRequest(BaseModel):
	field: TaskField
	value: str
