

while True:
    try:
        idade = int(input('Digite a sua idade: '))
        print('Idade salva na memória.')
        break
    except ValueError:
        print('Erro: digite uma idade válida.')
    except ZeroDivisionError:
        print('Idade não pode ser igual a zero.')
    except
        print('Erro: erro não identificado, contate o admnistrador do sistema')
        break

#if idade.isnumeric():
#   idade = int(idade)
#else:
#   print('Erro: Digite uma idade válida.')
#   exit()

try:
