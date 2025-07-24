from fastapi import APIRouter, Depends

from src.models.schemas import TaskCreateRequest, TaskListResponse, TaskStatus, TaskEditRequest
from src.models.objects import TaskObject
import src.controllers.tasks as controller
from src.controllers.auth import validate_user_token

router = APIRouter(prefix="/tasks", dependencies=[Depends(validate_user_token)])


@router.post("/create")
async def create_task(form: TaskCreateRequest):
	return await controller.create(
		title=form.title,
		description=form.description,
		status=form.status
	)


@router.get("/list", response_model=TaskListResponse)
async def list_tasks(status: TaskStatus | None = None):
	tasks_list: list[TaskObject] = await controller.get_list(status=status)
	return TaskListResponse(tasks=tasks_list)


@router.patch("/edit")
async def edit_task(task_id: int, form: TaskEditRequest):
	await controller.edit_task(
		task_id=task_id,
		field=form.field,
		value=form.value
	)


@router.delete("/delete")
async def delete_task(task_id: int):
	await controller.delete_task(task_id=task_id)
