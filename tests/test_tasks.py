def test_create_task(client, auth_headers):
    response = client.post("/api/v1/tasks/", json={
        "title": "My Task",
        "description": "Test",
        "status": "TODO"
    }, headers=auth_headers)
    assert response.status_code == 201
    assert response.json()["title"] == "My Task"

def test_get_my_tasks(client, auth_headers):
    response = client.get("/api/v1/tasks/my", headers=auth_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_task_without_token(client):
    response = client.post("/api/v1/tasks/", json={"title": "Task"})
    assert response.status_code == 403

def test_update_task(client, auth_headers):
    create = client.post("/api/v1/tasks/",
        json={"title": "Old"},
        headers=auth_headers)
    task_id = create.json()["id"]
    response = client.put(f"/api/v1/tasks/{task_id}",
        json={"title": "New", "status": "DONE"},
        headers=auth_headers)
    assert response.status_code == 200
    assert response.json()["status"] == "DONE"

def test_delete_task(client, auth_headers):
    create = client.post("/api/v1/tasks/",
        json={"title": "Delete me"},
        headers=auth_headers)
    task_id = create.json()["id"]
    response = client.delete(f"/api/v1/tasks/{task_id}",
                              headers=auth_headers)
    assert response.status_code == 200