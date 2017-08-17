estado = 'player 1 turn'

while True:
    if estado == 'player 1 turn':
        # do things
        estado = 'player 2 turn'
        continue
    elif estado == 'player 2 turn':
        pass
    elif estado == 'end of game':
        pass
    else:
        print('ops, you did, it again!, get straight into nowhere!!')
