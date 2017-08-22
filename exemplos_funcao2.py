def tres():
    ret = 3
    return ret

def dobro(n):
    ret = 2*n
    return ret

def multiplicar_dois_numeros(x, y):
    ret = x*y
    return ret

def meu_sum(l):
    ret = 0
    for elemento in l:
        ret += elemento
    return ret

# funcao que multiplica uma lista 
def multiplica(l):
    ret = 1
    for elemento in l:
        ret *= elemento

    return ret

#print(tres())
#print(dobro(4))
#print(multiplicar_dois_numeros(5, 7))
#print(multiplica([2, 4]))
