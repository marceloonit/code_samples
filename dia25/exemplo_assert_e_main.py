#assert 1 == 1 # não dá nada
#assert 1 == 0 # dá erro, fecha o programa

# assert serve para sair do programa caso alguma condição não seja satisfeita
# é uma forma de debugar o programa - não deixar os asserts (comentar) no código final, para que o usuário não visualize os erros

num = int(input('Digite um número diferente de zero.'))

assert num != 0

print(100/num)

# ver exemplo:
# https://github.com/mcsalgado/git_time_spent_tracking/blob/master/git_time_spent_tracking.py

##########################################

#variável dunder (double under) - __name__ retorna '__main__' quando chamado no próprio arquivo
#já se eu estiver usando um módulo feito por mim (p.ex.: minhas_funcoes.py), retornará 'minhas_funcoes.py'

print(__name__)

#serve para ver se esse é o programa principal:
if __name__ == '__main__':
    print('Este é o programa principal.')
