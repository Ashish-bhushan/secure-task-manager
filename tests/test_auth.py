def test_register_success(client):
    response = client.post("/api/v1/auth/register", json={
        "name": "John Doe",
        "email": "john@test.com",
        "password": "password123"
    })
    assert response.status_code == 201
    assert "message" in response.json()

def test_register_duplicate_email(client):
    # Register once
    client.post("/api/v1/auth/register", json={
        "name": "John", "email": "dup@test.com", "password": "pass123"
    })
    # Register again with same email
    response = client.post("/api/v1/auth/register", json={
        "name": "John2", "email": "dup@test.com", "password": "pass123"
    })
    assert response.status_code == 400

def test_login_success(client):
    client.post("/api/v1/auth/register", json={
        "name": "Jane", "email": "jane@test.com", "password": "pass123"
    })
    response = client.post("/api/v1/auth/login", json={
        "email": "jane@test.com", "password": "pass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_wrong_password(client):
    response = client.post("/api/v1/auth/login", json={
        "email": "jane@test.com", "password": "wrongpass"
    })
    assert response.status_code == 401