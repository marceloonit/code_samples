# funcao que recebe uma lista de numeros e retorne uma nova lista com o dobro desses numeros

# lista mula
def dobra_item(l):
    ret = []
    for item in l:
        ret.append(item * 2)
    return ret

# sem lista mula
def dobra_item2(l):
    index = 0
    for item in l:
        l[index] = item * 2
        index += 1
    return l

# sem lista mula
def dobra_item3(l):
    for i in range(len(l)):
        l[i] = l[i] * 2
    return l

# A partir de uma lista conhecida de strings, filtrar e criar nova lista somente com palavras que comecem com a
def classifica_fruta(frutas):
    frutas_a = []
    for fruta in frutas:
        if fruta[0] == 'a':
            frutas_a.append(fruta)
    return frutas_a



frutas = ['maça', 'abacaxi', 'acerola', 'mamão', 'jabuticaba', 'carambola', 'tamarindo', 'amora']
l = [1, 2, 3]

print(dobra_item(l))
print(dobra_item2(l))
print(dobra_item3(l))
print('valro final de l: ' + str(l))
print('')
print(classifica_fruta(frutas))
