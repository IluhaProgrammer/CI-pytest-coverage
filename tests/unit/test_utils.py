import pytest
from app.utils import discount_price

def test_discount_price_ok():
    assert discount_price(100.0, 10) == 90.0

def test_discount_price_invalid_percent():
    with pytest.raises(ValueError):
        discount_price(100.0, 150)