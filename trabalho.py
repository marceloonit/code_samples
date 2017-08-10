#!/usr/bin/env python3

idade_media = 80

nome = input("Entre com o seu nome: ")
idade = input("Entre com a sua idade (anos): ")
while (not idade.isdigit()):
	idade = input("Idade deve ser em anos inteiros: ")

idade = int(idade)

print("Olá, " + nome + ", você tem apenas mais " + str(idade_media - idade) + " anos de vida!")
print("Boa vida!!")
