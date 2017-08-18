number = int(input('Digite o número que voce deseja calcular o fatorial: '))

def fatorar(n):
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return(fatorial)

def_result = fatorar(number)
print('O fatorial de ' + str(number) + ' é ' + str(def_result))

