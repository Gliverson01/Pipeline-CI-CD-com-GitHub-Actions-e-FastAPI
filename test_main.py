from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200  # nosec B101
    assert response.json() == {"message": "Hello, CI/CD with FastAPI!"}  # nosec B101


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200  # nosec B101
    assert response.json() == {"status": "ok"}  # nosec B101
