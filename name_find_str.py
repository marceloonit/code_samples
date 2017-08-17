#!/usr/bin/env python3

name = input('Digite o seu nome: ')


print('')
print('Seu nome é .......................... ' + str(name))
print('A primeira letra do seu nome é ...... ' + str(name[1]))
print('A ultima letra do seu nome é ........ ' + str(name[-1]))

count = 0
for index in range(len(name)):

    if index != 0:
        if name[index] == name[index -1]:
            count += 1

if count == 1:
    print('Você tem um encontro consonantal no seu nome!')
elif count > 1:
    print('Você tem mais de um  encontro consonantal no seu nome!')


vogal = []
count = 0
while True:
    if name[count] == 'a' or name[count] == 'e' or name[count] == 'i' or name[count] == 'o' or name[count] == 'u':
        vogal = vogal + list(name[count])
    if count == len(name) - 1:
        break
    count += 1

if len(vogal) > 0:
    print('As vogais do seu nome são: ' + str(vogal))

