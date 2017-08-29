import random
## magic dunder 
class Iate(object):
    def __init__(self):
        self.nome = ''
        self.esta_ligado = False
        self.hp = 1000000
        print('O Iate foi criado')

    def dar_nome(self, nome):
        self.nome = nome

    def ligar(self):
        if self.esta_ligado:
            print('O {0} já está ligado!'.format(self.nome))
        else:
            self.esta_ligado = True
            print('O Iate foi ligado!')

    def flutuar(self):
        print('Este Iate está flutuando. Nossa que legal.')

    def atacar(self, alvo):
        alvo.hp -= 100
        print('{0} atacou {1}'.format(self.nome, alvo.nome))
        if alvo.hp < 1:
            print(alvo.nome, 'está morto!')
            alvo.status = 'morto'

class Bone(object):
    def __init__(self):
        self.hp = 10
        self.nome = 'Boné MAGA'

    def usar(self, alvo):
        if self.status == 'morto':
            print('Você não pode usar', self.nome, ', ele está morto.')
        else:
            print('{1} pode usar {0}'.format(alvo.nome, self.nome))


class Voce(object):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def usar(self, coisa):
        id coisa.status == 'morto':
            print()
        

veronica = Iate()
lola = Iate()

lola.dar_nome('lolaaaaa')
print(lola.nome)
lola.dar_nome('oi')
print(lola.nome)


import code
code.interact(local=locals())
