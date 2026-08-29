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
    """Split total into per-person shares (in cents-rounded currency units).

    Naively dividing and rounding each share independently can make the
    shares fail to add back up to the original total (e.g. splitting
    $10 three ways as 3.33 each only sums to $9.99). Instead, split the
    total in whole cents and hand out any leftover cents one at a time
    so the shares always sum exactly to the (rounded) total.
    """
    if people <= 0:
        raise ValueError("people must be greater than 0")
    total_cents = round(total * 100)
    base_cents, remainder_cents = divmod(total_cents, people)
    shares_cents = [base_cents + (1 if i < remainder_cents else 0) for i in range(people)]
    return [round(cents / 100, 2) for cents in shares_cents]