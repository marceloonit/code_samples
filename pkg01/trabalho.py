#!/usr/bin/env python3

import time

idade_media = 80

nome = input("Entre com o seu nome: ")
idade = input("Entre com a sua idade (anos): ")
while (not idade.isdigit()):
	idade = input("Idade deve ser em anos inteiros: ")

idade = int(idade)

restante = idade_media - idade

contador = restante

print("Olá, " + nome + ", você tem apenas mais " + str(restante) + " anos de vida!")
for i in range((restante)):
	print(str(restante - i))
	time.sleep(1)
