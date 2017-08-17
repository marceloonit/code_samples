#!/usr/bin/env python3
# source code: https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input

import random, sys

def yes_or_no(answer, default="yes"):

    valid = {"yes": True, "y": True, "ye": True,
            "no": False, "n": false}

    if default is None:
        prompt = " [y/n]"
    elif default == "yes":
        prompt = " [Y/n]"
    elif default == "no":
        prompt = " [y/N]"
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return










while True:
    try:
        guess = 0
        while (guess < 1 or guess > 6 or guess != dice):
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
