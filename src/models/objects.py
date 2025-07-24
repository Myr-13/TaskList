from pydantic import BaseModel, ConfigDict


class TaskObject(BaseModel):
	model_config = ConfigDict(from_attributes=True)

	id: int
	title: str
	description: str
	status: str
