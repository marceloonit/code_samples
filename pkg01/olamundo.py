#!/usr/bin/python3

import numbers

name = input("What's your name: ")
age = input("Idade? (em anos): ")


#while [[ ! age.isdigit() ]]
#if age.isdigit():
#	print("if - ok")
#not isinstance(age, numbers.Integral)
#	print("is - ok ")
while (not age.isdigit()):
	age = input("Idade deve ser em anos inteiros: ")


print("Nice to meet you " + name + "!")
print("Ola Mundo!, você tem " + age + " anos.")
