#!/usr/bin/env python3

# largura da caixa
largura = int(input("Digite a largura da caixa: "))
# altura da caixa
altura = 10

print("-" * largura)

for i in range(altura):
	print("|" + " " * (largura - 2) + "|")

print("-" * largura)
