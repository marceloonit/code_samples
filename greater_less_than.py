#!/usr/bin/env python3

# Ecxercise of greater and less than operators

nome = input('Nome: ')

if nome == 'Apolo':
    print('Eu não gosto de você!!')
    exit()

while True:
    try:
        money = -1
        while money < 0:
            money = float(input("Enter how much do you have in your bank account: "))
        break
    except ValueError:
        print("Value not valid, try again.")


if money < 1000000:
    print("You are not Donaldo Duck's uncle")
elif money < 2000000:
    print("you are getting there!!")
else:
    print("YOU ARE DONALD DUCK's UNCLE!!")

