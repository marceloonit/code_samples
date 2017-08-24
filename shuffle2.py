def shuffle_list(len_, chosen_port):
    list_doors = ['iate'] + ['bone'] * (len_ - 1)
    random.shuffle(list_doors)
    opened_doors = []
    lista = []
# open all doors less if iate is not the chosen door (iate and chosen door) or if iate is the chosen door (chosen door + 1 door)
    if list_doors[chosen_port] != 'iate':
        port_number = 1
        for door in list_doors:
            #if door != 'iate' and (list_doors.index(door) + 1) != chosen_port:
            #print(door)
            print(str(port_number) + ': ' + str(door))
            #else:
             #   print(str(list_doors.index(door) + 1) + ': XXXX')
            port_number += 1
        else:
            for 

           lista1 = list(range(0, chosen_port))
           lista2 = list(range(chosen_port - 1, len_))


    return None
import random

print(shuffle_list(3, 2))
