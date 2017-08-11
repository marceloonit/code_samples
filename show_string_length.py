#!/usr/bin/env python3

string = input("Enter the string to be analyzed (spaces will be cut off): ")
string = string.replace(" ","")
print('The length of "' + string + '" is: ' + str(len(string)))
