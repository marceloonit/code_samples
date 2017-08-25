exemplo = '(()'

lista = []
for letra in examplo:
    if letra == '(':
        lista.append('(')
    elif letra == ')':
        resultado_do_pop = lista.pop()
        if resultado_do_pop != '(':
            print('ocorreu um erro')
            exit()

if len(list) > 0:
    print('ocorreu um erro')
else:
    print('string validada com sucesso')
