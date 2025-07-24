from fastapi import HTTPException
from sqlalchemy import select, func, Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.schemas import TaskStatus, TaskField
from src.models.objects import TaskObject
from src.models.database import Task
from src.base.database import get_session_maker


async def create(*, title: str, description: str, status: TaskStatus) -> None:
	async with get_session_maker()() as session:
		session: AsyncSession

		# Check for task with given name
		db_result: Result = await session.execute(select(func.count()).where(Task.title == title))
		count: int = db_result.scalar()
		if count != 0:
			raise HTTPException(status_code=400, detail="Task with given title already exists")

		# Add new task
		task = Task(
			title=title,
			description=description,
			status=status
		)
		session.add(task)
		await session.commit()


async def get_list(*, status: TaskStatus | None) -> list[TaskObject]:
	out_tasks_list: list[TaskObject] = []

	async with get_session_maker()() as session:
		session: AsyncSession

		if status is not None:
			db_result: Result = await session.execute(select(Task).where(Task.status == status))
		else:
			db_result: Result = await session.execute(select(Task))
		tasks = db_result.scalars().all()

		for task in tasks:
			task: Task
			out_tasks_list.append(TaskObject.model_validate(task))

	return out_tasks_list


async def edit_task(*, task_id: int, field: TaskField, value: str):
	async with get_session_maker()() as session:
		session: AsyncSession

		db_result: Result = await session.execute(select(Task).where(Task.id == task_id))
		task: Task | None = db_result.scalars().first()

		if task is None:
			raise HTTPException(status_code=404, detail="Task not found")

		try:
			if field == TaskField.STATUS:
				value = TaskStatus(value)
		except ValueError:
			raise HTTPException(status_code=400, detail="Invalid field status value")

		setattr(task, field, value)
		await session.commit()


async def delete_task(*, task_id: int):
	async with get_session_maker()() as session:
		session: AsyncSession

		db_result: Result = await session.execute(select(Task).where(Task.id == task_id))
		task: Task | None = db_result.scalars().first()

		if task is None:
			raise HTTPException(status_code=404, detail="Task not found")

		await session.delete(task)
		await session.commit()
