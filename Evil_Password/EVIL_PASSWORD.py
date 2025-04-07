import random
import time

# probaility is 1/71,721,955

list1 = ["1234","1111","9876","pass","0000"]

print('The first password is one of these:', list1)
print()
print('Password 2 is one of the ones from the rockyou.txt file')
print()

with open("rockyou.txt", "rb") as file:
    rockyou = file.readlines()

time.sleep(3)

while True:

    sel1 = random.randint(0,len(list1)-1)
    password1 = list1[sel1]
    guess1 = input("Password1: ")

    if guess1 == password1:
        print("Correct! Now guess the second password.")
        sel2 = random.randint(0,len(rockyou)-1)
        password2 = rockyou[sel2].decode("utf-8").strip()

        guess2 = input("Password2: ")

        if guess2 == password2:
            print("Nice Guess. Here is the password for the next container: <||||||>")
            break

        else:
            print("Not even close. Restarting...")
    else:
        print("Nope. Restarting...")
