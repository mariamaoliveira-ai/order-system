from unittest.mock import Mock
import pytest
from sqlalchemy.exc import OperationalError

from app.main import app
from app.controllers.order_controller import getOrderService
from app.schemas import OrderResponse


@pytest.fixture
def mockOrderService():
    mockService = Mock()
    
    app.dependency_overrides[getOrderService] = lambda: mockService
    
    yield mockService
    
    app.dependency_overrides.clear()



def test_shouldReturnConfirmationWhenOrderIsCreatedSuccessfully(client, mockOrderService) -> None:
    mockOrderService.createOrder.return_value = OrderResponse(id=42, status="PENDING")
    
    response = client.post(
		"/orders/create",
		json={"items": "1x Camiseta, 2x Calças"},
	)
    
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 42
    assert body["status"] == "PENDING"
    mockOrderService.createOrder.assert_called_once()


def test_shouldReturnValidationErrorWhenOrderItemsAreEmpty(client) -> None:
	response = client.post("/orders/create", json={"items": ""})

	assert response.status_code == 422
	assert response.json()["detail"]


def test_shouldReturnServiceUnavailableWhenOrderBackendIsDown(client, mockOrderService) -> None:
    mockOrderService.createOrder.side_effect = OperationalError("DB is down", 
                                                                params=None, 
                                                                orig=None)
    
    response = client.post("/orders/create", json={"items": "1x Livro"})

    assert response.status_code == 503
    assert response.json() == {
        "detail": "Connection Error."
    }
