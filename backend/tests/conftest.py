import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

@pytest.fixture
def client():
    # Initialized here and passed to test functions automatically
    with TestClient(app) as test_client:
        yield test_client