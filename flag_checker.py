import hashlib
import random

# Get flag number while filtering bad inputs
while True:

    try:
        flag_num = int(input("flag number?: "))
    except ValueError:
        print("try a real number")
        print()
        continue
    if flag_num > 10  or flag_num < 0:
        print("not a real flag")
        print()
    else:
        print()
        break

# test for pulling working md5 - DELETE LATER
flag = input("flag: ")
md5 = hashlib.md5(flag.encode()).hexdigest()
print(md5)

# List of flags in order to be pulled - REPLACE LATER
flag_hash = [
    "a",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
]

# Hashes of the actual flags - DELETE LATER
flag_hash[0] = "0cc175b9c0f1b6a831c399e269772661"
flag_hash[1] = ""
flag_hash[2] = ""
flag_hash[3] = ""
flag_hash[4] = ""
flag_hash[5] = ""
flag_hash[6] = ""
flag_hash[7] = ""
flag_hash[8] = ""
flag_hash[9] = ""
flag_hash[10] = ""
flag_hash[11] = ""
flag_hash[12] = ""
flag_hash[13] = ""
flag_hash[14] = ""

# List of "Nopes"
nopes = [
    "Not quite, try again!",
    "That's not it.",
    "Good guess, but nope!",
    "Close, but not exactly!",
    "Not quite, but you're on the right track!",
    "That's not the one, but nice try!",
    "Nope, not this time!",
    "Almost, but not quite!",
    "Not exactly, but keep going!",
    "That's incorrect, but you're getting closer!",
    "Try again, but you're warm!",
    "Wrong answer, but you're thinking in the right direction!",
    "Close, but still not it!",
    "Nope, but keep guessing!",
]

# Get input for flag or print "nope"
while True:

    answer = input("flag?: ")

    if hashlib.md5(answer.encode()).hexdigest() == flag_hash[int(flag_num) - 1]:
        print("Conratulations! That is correct!")
        break
    else:
        response = random.randint(1,15)
        print(nopes[int(response) - 1])
        print()
