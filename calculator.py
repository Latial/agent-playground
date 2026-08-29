def calculate_average(numbers):
    """Return the arithmetic mean of numbers, or 0.0 if the list is empty."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def parse_price(text):
    cleaned = text.replace("$", "").strip()
    if "," in cleaned and "." not in cleaned:
        cleaned = cleaned.replace(",", ".")
    return float(cleaned)

def apply_discount(price, percent):
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return price - (price * percent / 100)

def split_bill(total, people):
    return round(total / people, 2)