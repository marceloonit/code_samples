# fizzbuzz
# imprima numeros de 1 a 100
# se o numero for divisivel por 2 imprima fizz
# se o numero for divisivel por 3 imprima fizz
# se o numero for divisivel por 2 e 3 imprima fizzbuzz


for i in range(1, 101):
    if i % 2 == 0 and i % 3 == 0:
        print('fizzbuzz')
    elif i % 2 == 0:
        print('fizz')
    elif i % 3 == 0:
        print('buzz')
    else:
        print(i)


