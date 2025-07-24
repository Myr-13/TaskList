import pytest

from fastapi.testclient import TestClient

from src.app import app

test_client = TestClient(app)
# Don't have any actual payload
test_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzcxNTQxMzYxLCJpYXQiOjE3NTMzOTczNjF9.D9nfPHnWSwnsuyN_ZoR6Wga9QiLQ-JN9-sNPwIlRTRs"


@pytest.mark.asyncio
async def test_create_item(database):
	res = test_client.post("/tasks/create", headers={"Authorization": f"Bearer {test_token}"}, json={
		"title": "testing",
		"description": "testing_description",
		"status": "pending"
	})
	assert res.status_code == 200

	res = test_client.post("/tasks/create", headers={"Authorization": f"Bearer {test_token}"}, json={
		"title": "testing",
		"description": "testing",
		"status": "done"
	})
	assert res.status_code == 400


@pytest.mark.asyncio
async def test_get_tasks(database):
	res = test_client.post("/tasks/create", headers={"Authorization": f"Bearer {test_token}"}, json={
		"title": "testing",
		"description": "testing_description",
		"status": "pending"
	})
	assert res.status_code == 200

	res = test_client.get("/tasks/list", headers={"Authorization": f"Bearer {test_token}"})
	assert res.status_code == 200
	assert len(res.json()["tasks"]) == 1
	assert res.json()["tasks"][0]["title"] == "testing"


@pytest.mark.asyncio
async def test_delete_task(database):
	res = test_client.post("/tasks/create", headers={"Authorization": f"Bearer {test_token}"}, json={
		"title": "testing",
		"description": "testing_description",
		"status": "pending"
	})
	assert res.status_code == 200
	task_id = res.json()["id"]

	res = test_client.delete("/tasks/delete", headers={"Authorization": f"Bearer {test_token}"}, params={
		"task_id": task_id
	})
	assert res.status_code == 200

	res = test_client.get("/tasks/list", headers={"Authorization": f"Bearer {test_token}"})
	assert res.status_code == 200
	assert len(res.json()["tasks"]) == 0
