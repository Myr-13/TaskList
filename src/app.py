import contextlib
import logging

from fastapi import FastAPI
from decouple import config

from src.routers.auth import router as auth_router
from src.routers.tasks import router as task_list_router
from src.base.database import initialize_db


@contextlib.asynccontextmanager
async def lifespan(app: FastAPI):
	# Init database
	try:
		await initialize_db(
			user=config("DATABASE_USER"),
			password=config("DATABASE_PASSWORD"),
			ip=config("DATABASE_IP"),
			database_name=config("DATABASE_NAME")
		)
	except ConnectionRefusedError as e:
		logging.error(e)
		raise RuntimeError("Database connection failed")

	# Continue startup
	yield


app = FastAPI(lifespan=lifespan)

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app.include_router(auth_router)
app.include_router(task_list_router)
