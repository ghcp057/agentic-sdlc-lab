from unittest.mock import MagicMock

import pytest

from app.modules.orders import models, repository, service
from app.modules.orders.exceptions import OrderOwnershipError
from app.modules.orders.service import InvalidOrderTransition, OrderStateMachine


def test_returned_is_order_status():
    assert models.OrderStatus.RETURNED.value == "returned"


def test_delivered_can_transition_to_returned():
    OrderStateMachine.validate_transition(
        models.OrderStatus.DELIVERED,
        models.OrderStatus.RETURNED,
    )


def test_returned_is_terminal():
    assert OrderStateMachine.is_terminal(models.OrderStatus.RETURNED)


def test_delivered_is_not_terminal_while_return_is_allowed():
    assert not OrderStateMachine.is_terminal(models.OrderStatus.DELIVERED)


def test_returned_cannot_transition_to_another_status():
    with pytest.raises(InvalidOrderTransition):
        OrderStateMachine.validate_transition(
            models.OrderStatus.RETURNED,
            models.OrderStatus.CANCELLED,
        )


def test_cancel_order_refuses_returned_order():
    repo = MagicMock(spec=repository.OrderRepository)
    order = MagicMock(spec=models.Order)
    order.status = models.OrderStatus.RETURNED
    repo.get_order.return_value = order
    db = MagicMock()

    with pytest.raises(OrderOwnershipError):
        service.cancel_order(db, repo, 1)

    db.commit.assert_not_called()


def test_cancel_order_refuses_delivered_order():
    repo = MagicMock(spec=repository.OrderRepository)
    order = MagicMock(spec=models.Order)
    order.status = models.OrderStatus.DELIVERED
    repo.get_order.return_value = order
    db = MagicMock()

    with pytest.raises(OrderOwnershipError):
        service.cancel_order(db, repo, 1)

    db.commit.assert_not_called()
