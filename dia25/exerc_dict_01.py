d = {'a':'d', 
     'e':'f', 
     'r':'t', 
     's':'y'}

texto = input('Digite um texto qualquer:\n')

result = ''

for caracter in texto:
    if caracter in d.keys():
        result += d[caracter]
    else:
        result += caracter

print(result)

####################################

result = ''

for caracter in texto:
    result += d.get(caracter, caracter) # busca o caracter (1º arg.) no dicionário - se não tiver, retorna o próprio caracter (2º arg.)

print(result)
