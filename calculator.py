def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def parse_price(text):
    return float(text.replace("$", ""))