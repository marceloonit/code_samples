import random

#painel = ['iate', 'boné', 'boné']
#random.shuffle(painel)
#print(painel)

####################################################

print('\n'*2)

class Iate(object):
    def __init__(self): # aqui vão os valores padrão dos atributos!!!
        self.ligado = False # sempre colocar o self.
        self.temperatura = 10
        self.molhado = False
        self.energia = 1000
        print('Iate foi iniciado.')
    def ligar(self): # método #o primeiro argumento é sempre o PRÓPRIO OBJETO (convenção de nome é: self)
        self.ligado = True # atribui True ao atributo 'ligado'
        self.temperatura = 80
        print('Iate foi ligado.')
    def desligar(self):
        self.ligado = False
        self.temperatura = 10
        print('Iate foi desligado.')
    def flutuar(self):
        self.molhado = True
        print('Este iate está flutuando. Nossa, que legal!')
    def darnome(self, nome_dado):
        self.nome = nome_dado
    def atacar(self, alvo):
        alvo.energia -= 100
        print('{0} atacou o alvo {1}.'.format(self.nome, alvo.nome))
    def info(self):
        print('Ligado: ', self.ligado)
        print('Temperatura: ', self.temperatura)
        print('Molhado: ', self.molhado)

class Bone(object):
    pass

#iate = Iate() #declarando um objeto do TIPO Iate
#bone1 = Bone() #declarando um objeto do TIPO Bone
#bone2 = Bone() #declarando um objeto do TIPO Bone

#import code
#code.interact(local=locals())

veronica = Iate()
#veronica.ligar()
veronica.cor = 'vermelho' #atributo definido em tempo de execução

lola = Iate()
#veronica.ligar()
lola.cor = 'azul'

veronica.darnome('Verônica')
lola.darnome('Lola')

veronica.atacar(lola)

print('\n'*2)

import code
code.interact(local=locals())
