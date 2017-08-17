#!/usr/bin/env python3

num1 = int(input('Insert number one: '))
num2 = int(input('Insert number two: '))
num3 = int(input('Insert number three: '))
#max_ = max(num1, num2)

#print("The biggest number is (via max): " + str(max_))
###############################

#if num1 == num2:
#    message = "The numbers are equal: " + str(num1)

#if num1 > num2:
#    message = "The number one is the biggest one: " + str(num1)


#if num1 < num2:
#    message = "The number two is the biggest one: " + str(num2)

#print(message)

##########################################

if num1 > num2 > num3:
    print("Number 1 is the biggest" + str(num1))

if num1 > num3 > num2:
    print("Number 1 is the biggest" + str(num1))

if num2 > num1 > num3:
    print("Number 2 is the biggest" + str(num2))

if num2 > num3 > num1:
    print("Number 2 is the biggest" + str(num2))

if num3 > num1 > num2:
    print("Number 3 is the biggest" + str(num3))

if num3 > num2 > num1:
    print("Number 3 is the biggest" + str(num3))


if num2 == num1 > num3:
    print(num1)

if num2 == num1 < num3:
    print(num3)


if num1 == num3 and num1 > num2:
    print(num1)

if num1 == num3 and num1 < num2:
    print(num2)
    
if num3 == num2 and num1 > num3:
    print(num1)

if num3 == num2 and num1 < num3:
    print(num3)

if num1 == num2 == num3:
    print(num1)
