from fastapi.testclient import TestClient

from git_day_practice.api import app
from git_day_practice.settings import settings

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_config():
    response = client.get("/config")
    assert response.status_code == 200
    assert "API_KEY" not in response.json()
    assert response.json().get("APP_NAME") == settings.APP_NAME


def test_secure_data_unauthorized():
    response = client.get("/secure-data")
    assert response.status_code == 401


def test_secure_data_authorized():
    response = client.get("/secure-data", headers={"X-API-Key": settings.API_KEY})
    assert response.status_code == 200
    assert response.json() == {"data": "This is secure data!"}
