#!/usr/bin/env python3

#
# Classic exercise of a gradebook ...
#

import os
os.system('clear')

notas = []

nome_aluno = input("Entre com o nome do aluno: ")

while True:
	try:
		qtde_de_notas = int(input("Entre com a quantidade de notas: "))
		break
	except ValueError:
		print("Deve ser um número inteiro, tente novamente: ")

for i in range(qtde_de_notas):
	while True:
		try:
			print("Nota " + str(i + 1))
			notas = notas + [float(input())]
			break
		except ValueError:
			print("Numeros racionais, por favor!! tente novamente.")

os.system('clear')

count = 1
total = 0

print("Aluno: " + nome_aluno)
for each in notas:
	print("Nota " + str(count) + ": " + str(each))
	count = count + 1
	total = total + each

print("Média final: " + str(total / qtde_de_notas))

