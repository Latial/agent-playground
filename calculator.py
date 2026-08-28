def calculate_average(numbers):
    """Return the arithmetic mean of numbers, or 0.0 if the list is empty."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def parse_price(text):
    return float(text.replace("$", ""))