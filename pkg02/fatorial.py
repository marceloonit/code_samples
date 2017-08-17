#!/usr/bin/env python3
# Fatorar número
n = int(input('Digite o número que você deseja calcular o fatorial: '))

fatorial = 1
for i in range(n):
    fatorial = fatorial * (i + 1)

print(str(n) + "! é " + str(fatorial))

