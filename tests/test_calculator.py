from calculator import calculate_average, parse_price

def test_average():
    assert calculate_average([2, 4, 6]) == 4

def test_parse_price():
    assert parse_price("$3.50") == 3.5