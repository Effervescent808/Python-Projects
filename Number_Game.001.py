import random

number = random.randint(1,100)
attempts = 1

print('Guess a number between 1 and 100.')

while True:
    
    try:
        guess = int(input('Guess: '))
    except ValueError:
        guess = ""
        print('Try guessing a real number')
        continue

    if guess == number:
        print('Yay, you won!') 
        print('attempts:',attempts)
        break
    elif number > guess:
        print('To low, try something higher')
        attempts += 1
    else:
        print ('To high, try something lower')
        attempts += 1

