from unittest.mock import Mock
import pytest

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


# def should_return_validation_error_when_order_items_are_empty() -> None:
# 	response = client.post("/orders/create", json={"items": ""})

# 	assert response.status_code == 422
# 	assert response.json()["detail"]


# def should_return_service_unavailable_when_order_backend_is_down(monkeypatch) -> None:
# 	order_service = Mock()
# 	order_service.create_order.side_effect = BackendUnavailableError("database unavailable")
# 	monkeypatch.setitem(app.dependency_overrides, get_order_service, lambda: order_service)

# 	response = client.post("/orders/create", json={"items": "1x Livro"})

# 	assert response.status_code == 503
# 	assert response.json() == {
# 		"detail": "Não foi possível realizar o pedido. Tente novamente mais tarde."
# 	}
