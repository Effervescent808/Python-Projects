import random
import string

Key = random.randint(1,9)

ShowKey = True

String = input('String: ')

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + (Key + 1)

output = []

for letter in String:
    nLetter = letter.lower()
    if nLetter in values:
        output.append(str(values[nLetter]))

print("".join(output))

if ShowKey == True:
    print(Key)