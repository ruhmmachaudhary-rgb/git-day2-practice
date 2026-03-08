import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add src/ to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

# Import FastAPI app
from git_day_practice.api import app

@pytest.fixture(scope="session")
def client() -> TestClient:
    """
    Create one TestClient for the test session.
    Also sets required env vars so pydantic-settings doesn't fail.
    """
    os.environ.setdefault("API_KEY", "test-key")
    os.environ.setdefault("APP_NAME", "Test API")
    os.environ.setdefault("ENVIRONMENT", "test")
    os.environ.setdefault("DEBUG", "false")
    return TestClient(app)