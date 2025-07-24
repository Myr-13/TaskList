from fastapi import APIRouter

from src.models.schemas import LoginRequest
import src.controllers.auth as controller

router = APIRouter(prefix="/task_list")


@router.post("/create")
async def login(form: LoginRequest):
	return await controller.login(
		username=form.username,
		password=form.password
	)
