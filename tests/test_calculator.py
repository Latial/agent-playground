import pytest

from calculator import apply_discount, calculate_average, parse_price

def test_average():
    assert calculate_average([2, 4, 6]) == 4

def test_average_empty_list():
    assert calculate_average([]) == 0.0

def test_parse_price():
    assert parse_price("$3.50") == 3.5

def test_parse_price_european_comma_decimal():
    assert parse_price("3,50") == 3.5

def test_apply_discount():
    assert apply_discount(100, 20) == 80

def test_apply_discount_rejects_percent_above_100():
    with pytest.raises(ValueError):
        apply_discount(100, 150)

def test_apply_discount_rejects_negative_percent():
    with pytest.raises(ValueError):
        apply_discount(100, -20)