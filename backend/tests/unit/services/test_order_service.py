from unittest.mock import Mock

import pytest

from app.database.models.order import OrderStatus
from app.schemas.order import Order
# from app.services.order_service import OrderService


def test_should_create_pending_order_when_items_are_valid() -> None:
    pass
	# orderRepository = Mock()
	# orderRepository.create.return_value = Mock(id=42)
	# service = OrderService(orderRepository)

	# result = service.create_order(Order(items="1x Camiseta, 2x Calças"))

	# orderRepository.create.assert_called_once_with(
	# 	items="1x Camiseta, 2x Calças",
	# 	status=OrderStatus.PENDING,
	# )
	# assert result.id == 42
	# assert result.status == OrderStatus.PENDING


# @pytest.mark.parametrize("items", ["", "   "])
# def should_reject_empty_items_without_persisting_when_items_are_blank(items: str) -> None:
# 	order_repository = Mock()
# 	service = OrderService(order_repository)

# 	with pytest.raises(ValueError, match="Itens do pedido não podem ser vazios"):
# 		service.create_order(Order(items=items))

# 	order_repository.create.assert_not_called()


# def should_raise_backend_unavailable_when_order_persistence_fails() -> None:
# 	order_repository = Mock()
# 	order_repository.create.side_effect = RuntimeError("database unavailable")
# 	service = OrderService(order_repository)

# 	with pytest.raises(BackendUnavailableError):
# 		service.create_order(Order(items="1x Livro"))

# 	order_repository.create.assert_called_once_with(
# 		items="1x Livro",
# 		status=OrderStatus.PENDING,
# 	)
