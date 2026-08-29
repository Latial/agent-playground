def calculate_average(numbers):
    """Return the arithmetic mean of numbers, or 0.0 if the list is empty."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def parse_price(text):
    return float(text.replace("$", ""))

def apply_discount(price, percent):
    return price - (price * percent / 100)

def split_bill(total, people):
    return round(total / people, 2)