
nomes = ['Arthur', 'Edson', 'Henrique', 'Luiz', 'Marcelo', 'Raphael', 'Rudney', 'Suelen']
tamanho_nomes = len(nomes)

# pattern do acumulador
#i = 0
#while i < tamanho_nomes:
#    print(nomes[i] + ' está aqui') 
#    i += 1

for nome in nomes:
    print('')
    print(nome + ' ............................. está aqui.')
    print('A primeira letra do seu nome é ...... ' + str(nome[0]))
    print('A ultima letra do seu nome é ........ ' + str(nome[-1]))

    count = 0
    for index in range(len(nome)):

        if index != 0:
            if nome[index] == nome[index -1]:
                count += 1

    if count == 1:
        print('Você tem um encontro consonantal no seu nome!')
    elif count > 1:
        print('Você tem mais de um  encontro consonantal no seu nome!')


    vogal = []
    consoante = []
    count = 0
    while True:
        if nome[count].lower() == 'a' or nome[count].lower() == 'e' or nome[count].lower() == 'i' or nome[count].lower() == 'o' or nome[count].lower() == 'u':
            vogal = vogal + list(nome[count])
        else:
            consoante = consoante + list(nome[count])
        if count == len(nome) - 1:
            break
        count += 1

    if len(vogal) > 0:
        print('As vogais do seu nome são ........... ' + str(vogal))
    if len(consoante) > 0:
        print('As consoantes do seu nome são ....... ' + str(consoante))

