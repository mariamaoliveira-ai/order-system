import pytest
from fastapi.testclient import TestClient
from app.main import app  # Import your FastAPI app instance

@pytest.fixture
def client():
    return TestClient(app, raise_server_exceptions=False)