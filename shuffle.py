#!/usr/bin/env python3

def open_door(choice):
    doors = ['iate', 'hat', 'hat']
    random.shuffle(doors)
    doors_support = doors.copy()
    print('LIST doors ' + str(doors))
    if doors.index(doors[choice - 1]) == doors.index('iate'):
        message = 'You just won an ' + str(doors[choice - 1].upper())
        return message
    else:
        doors_support.remove('iate')
        doors_support.remove(doors[choice - 1])

        #print(doors_support)
        print('One of the not chosen door has a ' + doors_support[0].lower())
        change = input("Do you want to change your door or do you want to keep it? (change/Keep)")
        if change == 'keep':
            message = 'Your choice is ' + str(choice) + ' just won an ' + str(doors[choice -1].upper())
            return message
        elif change == 'change':
            message = 'You just won an IATE in the door number ' + str(doors.index('iate') + 1)
            return message
    message = 'deu merda'
    return message

            
import random


#while True:

print("Choose a door from 1 to 3 and 0 to exit the program.")
choice = int(input("My choice is "))
print(open_door(choice))
