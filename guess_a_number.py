import random

secret_number = random.randrange(1,11)

i = 1

while True:

    try:

        guess = int(input("Guess a number between 1 and 10 : "))

        if guess != secret_number:
            i += 1

        elif guess == secret_number:
            print("Yaay! You guessed it! Secret number is {} and you guessed it {} times. " .format(secret_number, i))
            break

    except:
        print("Please enter a number. ")