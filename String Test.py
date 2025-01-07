import random

# String has to start empty
password = ""

# 10 is the number of numbers used
for _ in range(10):
    password += str(random.randint(1,9))

print(password)