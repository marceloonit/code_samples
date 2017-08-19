#!/usr/bin/env python3
import decimal
#### MEU ABS()

n = -5
l = "marcelo"
l_int = [1, 3, 8, 9, -9, 1]

def meu_abs(n):
        if n < 0:
            return(n * (- 1))
        else:
            return(n)

def raiz_quadrada(n):
    ret = n**(1/2)
    return ret

def meu_len(l):
    tamanho_lista = 0
    for item in l:
        tamanho_lista += 1
    return tamanho_lista

def meu_max(l_int):
    index = 0
    maior = ''
    for cada in l_int:
        if index == len(l_int) - 1:
            return maior
        
        if cada > l_int[index + 1]:
            if maior != '':
                if maior < cada:
                    maior = cada
            else:
                maior = cada
        else:
            if maior != '':
                if maior < l_int[index + 1]:
                    maior = l_int[index + 1]
            else:
                maior = l_int[index + 1]

        index += 1

def meu_min(l_int):
    index = 0
    menor = ''
    for cada in l_int:
        if index == len(l_int) - 1:
            return menor
        
        if cada < l_int[index + 1]:
            if menor != '':
                if menor > cada:
                    menor = cada
            else:
                menor = cada
        else:
            if menor != '':
                if menor > l_int[index + 1]:
                    menor = l_int[index + 1]
            else:
                menor = l_int[index + 1]

        index += 1

def meu_sum(l_int):
    ret = 0
    for numero in l_int:
        ret += numero

    return ret

def media(l_int):
    soma = meu_sum(l_int)
    ret = soma / len(l_int)
    return ret



print("abs ........... " + str(meu_abs(n)) + " de " + str(n))
print("raiz quadrada . " + str(raiz_quadrada(n)) + " de " + str(n))
print("len ........... " + str(meu_len(l)) + " de " + str(l))
print("max ........... " + str(meu_max(l_int)) + " de " + str(l_int))
print("min ........... " + str(meu_min(l_int)) + " de " + str(l_int))
print("sum ........... " + str(meu_sum(l_int)) + " de " + str(l_int))
print("media ......... " + str(media(l_int)) + " de " + str(l_int))


n = 5
l = "teste"
l_int = [1, 1, 1]
print("abs ........... " + str(meu_abs(n)) + " de " + str(n))
print("raiz quadrada . " + str(raiz_quadrada(n)) + " de " + str(n))
print("len ........... " + str(meu_len(l)) + " de " + str(l))
print("max ........... " + str(meu_max(l_int)) + " de " + str(l_int))
print("min ........... " + str(meu_min(l_int)) + " de " + str(l_int))
print("sum ........... " + str(meu_sum(l_int)) + " de " + str(l_int))
print("media ......... " + str(media(l_int)) + " de " + str(l_int))





#n = input("numero: ")

#while True:
#    if int != type(n) != float:
#        print("Tipo de dados nao suportado para ser calculado o valor absoluto.")
#        exit()
#    else:
#        result = meu_abs(n)
#        break
#print(result)

##### raiz quadrada



