import pytest
from pizza_order import pizza_price, order_discount, delivery_status


def test_pizza_price():
    assert pizza_price("medium", 0, False) == 350
    assert pizza_price("large", 4, True) == 750
    with pytest.raises(ValueError):
        pizza_price("xl", 1, False)
    with pytest.raises(ValueError):
        pizza_price("small", -1, False)
    with pytest.raises(ValueError):
        pizza_price("small", 1, True)


def test_order_discount():
    assert order_discount(200, "monday", False) == 0
    assert order_discount(400, "tuesday", True) == 250
    assert order_discount(400, "saturday", True) == 50
    assert order_discount(400, "monday", True) == 90


def test_delivery_status():
    assert delivery_status(20, 12) == "not deliverable"
    assert delivery_status(20, 3) == "on time"
    assert delivery_status(40, 3) == "late"
    assert delivery_status(50, 3) == "free pizza"
