import random

def generate_income(months=6):
    base = random.randint(15000, 30000)
    return [max(5000, base + random.randint(-7000, 7000)) for _ in range(months)]
