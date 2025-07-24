import contextlib
import logging

from fastapi import FastAPI

from src.routers.auth import router as auth_router
from src.routers.task_list import router as task_list_router
from src.base.database import initialize_db


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
	# Init config

	# Init database
	await initialize_db(
		user="",
		password="",
		ip="",
		database_name=""
	)

	yield


app = FastAPI(lifespan=lifespan)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app.include_router(auth_router)
app.include_router(task_list_router)
