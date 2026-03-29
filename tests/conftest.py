import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.db.base import Base
from app.db.session import get_db

# Use SQLite for tests — no PostgreSQL needed during testing!
TEST_DATABASE_URL = "sqlite:///./test.db"

engine_test = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)
TestSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine_test
)

# Create all tables in test database
Base.metadata.create_all(bind=engine_test)

def override_get_db():
    """Replace real DB with test DB during tests."""
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

# This line swaps the real DB for test DB
app.dependency_overrides[get_db] = override_get_db

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def auth_headers(client):
    """Creates a user, logs in, returns auth headers."""
    # Register
    client.post("/api/v1/auth/register", json={
        "name": "Test User",
        "email": "testuser@test.com",
        "password": "password123"
    })
    # Login
    response = client.post("/api/v1/auth/login", json={
        "email": "testuser@test.com",
        "password": "password123"
    })
    token = response.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}