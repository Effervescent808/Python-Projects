import string
import random

index = list(string.ascii_lowercase)
random.shuffle(index) 

for letter in index:
    print(letter)
