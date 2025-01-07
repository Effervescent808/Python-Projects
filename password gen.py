import random

Length = int(input("Length?: "))

symbols = "!@#$%&*"

letters = "abcdefghijklmnopqrstuvwxyz"

while True:
    Letters = input("Letters? y/n: ")
    if Letters == ('n'):
        letter_string = ""
        break

    elif Letters == ('y'):
        stringLength = random.randint(5,9)
        letter_string = "".join(random.choice(letters) for _ in range(stringLength))
        break

    else:
        print("Invalid Input")


while True:
    Symbols = input("Symbols? y/n: ")

    if Symbols == ('n'):
        symbol_string = ""
        break

    elif Symbols == ('y'):
        string_length = random.randint(5,9)
        symbol_string = "".join(random.choice(symbols) for _ in range(string_length))
        break

    else:
        print("Invalid Input")


number_string = ""

for _ in range(15):
    number_string += str(random.randint(1,9))

combined = letter_string + number_string + symbol_string 
pass_list = list(combined)
random.shuffle(pass_list)
password = "".join(pass_list)

print(password[:Length])