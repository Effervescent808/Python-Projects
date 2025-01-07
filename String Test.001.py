import random

symbols = "!@#$%&*"

string_length = random.randint(1,9)

symbol_string = "".join(random.choice(symbols) for _ in range(string_length))

print(symbol_string)