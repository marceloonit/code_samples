#!/usr/bin/env python3
import random





while True:
    try:
        guess = 0
        stop == 1
        while (guess < 1 or guess > 6):
            guess = int(input("Guess a number (1-6): "))
            if guess < 1:
                print("Números menores que 1 são inválidos. Try again.")
        break
    except ValueError:
        print("Invalid value, try again (1-6): ")

dice = random.randrange(1,7)

if guess == dice:
    print("You WON!!")

print("Your guess: " + str(guess) + ". Dice result: " + str(dice))
