from fastapi import APIRouter

from src.models.schemas import LoginRequest, LoginResponse
import src.controllers.auth as controller

router = APIRouter(prefix="/auth")


@router.post("/login", response_model=LoginResponse)
async def login(form: LoginRequest):
	token: str = await controller.login(
		username=form.username,
		password=form.password
	)

	return LoginResponse(token=token)
