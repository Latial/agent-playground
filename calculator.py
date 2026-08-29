def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def parse_price(text):
    return float(text.replace("$", ""))

def apply_discount(price, percent):
    return price - (price * percent / 100)

def split_bill(total, people):
    return round(total / people, 2)