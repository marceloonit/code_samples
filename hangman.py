#!/usr/bin/env python3

import getpass
import os

os.system('clear')
secret_word = getpass.getpass('Enter the word to be played with: ')
tamanho_word = len(secret_word)
tentativas = tamanho_word
list_secret_word = list(secret_word)
end = False
wrong = False
## body
#cabeca = 'O'
cabeca = ' '
#braco_direito = '/'
braco_direito = ' '
#braco_esquerdo = '\\'
braco_esquerdo = ' '
#tronco = '|'
tronco = ' '
#perna_direita = '/'
perna_direita = ' '
#perna_esquerda = '\\'
perna_esquerda = ' '

secret_list = ['*'] * int(len(secret_word))

while True:
    if end == True:
        break
    wrong = False
    guess = input('Enter a letter: ')
    
    if len(guess) != 1:
        continue
    
    if guess in secret_word:
        count = 0
        while count < len(secret_word):
            if guess == secret_word[count]:
                secret_list[count] = secret_word[count]
            count += 1
    else:
        tentativas -= 1
        if tentativas != 0:
 #           wrong = True

#    if wrong == True:
            if cabeca == ' ':
                cabeca = 'O'
            elif braco_direito == ' ':
                braco_direito = '/'
            elif tronco == ' ':
                tronco = '|'
            elif braco_esquerdo == ' ':
                braco_esquerdo = '\\'
            elif perna_direita == ' ':
                perna_direita = '/'
            elif perna_esquerda == ' ':
                perna_esquerda = '\\'

    if '*' not in secret_list:
        print("you WONNNN!!!")
        print(str(secret_list))
        break

    os.system('clear')    
    print('----------\n||       |\n||        ' + cabeca + '\n||       ' + braco_direito + tronco + braco_esquerdo + '\n||       ' + perna_direita + ' ' + perna_esquerda + '\n||\n||_____________')
    print(str(secret_list))
    if perna_esquerda == '\\':
        break

print("!!game over!!")
print('')
