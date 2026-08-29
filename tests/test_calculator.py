import pytest

from calculator import apply_discount, calculate_average, parse_price, split_bill

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

def test_split_bill_even_split():
    assert split_bill(100, 4) == [25.0, 25.0, 25.0, 25.0]

def test_split_bill_shares_add_up_to_total():
    # 10 / 3 = 3.333..., so naive per-share rounding (3.33 each) only
    # sums to 9.99. The shares returned must add up to the real total.
    shares = split_bill(10, 3)
    assert shares == [3.34, 3.33, 3.33]
    assert round(sum(shares), 2) == 10.0

def test_split_bill_rejects_non_positive_people():
    with pytest.raises(ValueError):
        split_bill(100, 0)