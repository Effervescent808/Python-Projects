import random
import string

Key = random.randint(1,9)

ShowKey = False

String = input('String: ').replace(" ", "^")

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
    values[letter] = index + (Key + 1)

output = []

for letter in String:
    nLetter = letter.lower()
    if nLetter in values and values[nLetter] >10:
        Number = (str(values[nLetter]))
        Output = Number[0] + '/' + Number[1]
        output.append(str(Output))

    elif nLetter in values and values[nLetter] <10:
        output.append(str(values[nLetter]))

    else:
        output.append(letter)

print("".join(output))

if ShowKey == True:
    print(Key)