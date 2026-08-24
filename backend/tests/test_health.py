from fastapi.testclient import TestClient

from order_system.main import app


client = TestClient(app)


def test_health_endpoint_reports_running_api() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
