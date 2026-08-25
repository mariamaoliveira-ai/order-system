from unittest.mock import Mock, MagicMock
from sqlalchemy.exc import OperationalError

import pytest

from app.database.models.order import OrderStatus, Order as OrderModel
from app.schemas.order import Order
from app.services import OrderService

@pytest.fixture
def mockDbSession():
    return MagicMock()

@pytest.fixture
def mockOrderService(mockDbSession):
    return OrderService(db=mockDbSession)
    

def test_shouldCreateOrder(mockOrderService, mockDbSession) -> None:
    def fake_refresh(obj):
        obj.id = 42
        obj.status = OrderStatus.PENDING
        
    mockDbSession.refresh.side_effect = fake_refresh

    orderInput = Order(items="1x Camiseta, 2x Calças")
    result = mockOrderService.createOrder(orderInput)
    
    assert mockDbSession.add.called
    assert mockDbSession.commit.called
    assert mockDbSession.refresh.called
    assert result.id == 42
    assert result.status == OrderStatus.PENDING


def test_shouldRaiseExceptionWhenDatabaseDown(mockOrderService, mockDbSession) -> None:
    mockDbSession.commit.side_effect = Exception("Database failure")

    orderInput = Order(items="1x Camiseta, 2x Calças")

    with pytest.raises(Exception):
        mockOrderService.createOrder(orderInput)

    # 3. Verify that add and commit were attempted, but refresh was never reached
    assert mockDbSession.add.called
    assert mockDbSession.commit.called
    assert mockDbSession.rollback.called
    assert not mockDbSession.refresh.called	


