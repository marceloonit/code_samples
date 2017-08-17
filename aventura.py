#!/usr/bin/env python3
"""aventura.py  - just a random exercise ... """

# NOTE(onit):
# TODO(onit):
# XXX(onit):

import time

lugar = 'Avatars Home'


while True:
    print('loading place')
    time.sleep(.2)
    print('.')
    time.sleep(.2)
    print('.')
    time.sleep(.1)
    print('.')
    if lugar == 'Avatars Home':
        print('You are at home now..')
        opcao_1 = 'Street'
        opcao_2 = 'In your pipe of your home o.O?'
        print('Suas opções: 1. ' + opcao_1 + ' 2. ' + opcao_2)
        opcao_escolhida = input('Digite sua opção: ')
        if opcao_escolhida == '1':
            lugar = opcao_1
            continue
        if opcao_escolhida == '2':
            lugar = opcao_2
            continue

    elif lugar == 'Iate':
        print("You WIIIINNNNN!!!!!!!")
        break
    elif lugar == 'Inferno':
        lugar = input("You are at the devils home, to where do you want to go?")
        continue
    elif lugar == 'Street':
        print("From here you may go forward in your life.")

        opcao_1 = 'Do Bank robery!'
        opcao_2 = 'Do math o.O?'
        opcao_3 = 'Do nothing, know nothing. :D'
        print('Suas opções: 1. ' + opcao_1 + ' 2. ' + opcao_2 + ' 3. ' + opcao_3)
        opcao_escolhida = input('Digite sua opção: ')
        if opcao_escolhida == '1':
            lugar = 'Cadeia'
            continue
            print(lugar)
        elif opcao_escolhida == '2':
            cronometro_comeco = time.time()
            resposta = int(input('Do the following math: 10 + 10: '))
            cronometro_fim = time.time()

            if cronometro_fim - cronometro_comeco > 10:
                print('You were too slow to answer ... to back to your home!!')
                lugar = 'Avatars Home'
                continue

            if resposta == 10 + 10:
                print(resposta)
                lugar = 'Iate'
                continue
            else:
                print("A conta te matou, mas tudo bem.")
                lugar = "Avatars Home"
                continue
        elif opcao_escolhida == '3':
            print("Voce nao fez nada.")
    elif lugar == 'In your pipe of your home o.O?':
        print('WOW, There is a mistery key')
        print('The key is a gift to you, take it and good luck!')
        tem_chave = True
        lugar = 'Avatars Home'
        continue

    elif lugar == 'Cadeia':
        print("Voce vai ficar para sempre aqui ....")

    elif lugar == 'Aventura':
        print("You were teletransported to another Universe. In this Universe there are only two dimensions.")
        print("it means you can only go back and forth.")
        input("Right now you are at the position ")
    else:
        print("You shouldnt be here ... bye!!")
        break
    print()
print('Game OVER!!')
