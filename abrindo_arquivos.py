#fp = open('text.txt')
#linhas_do_arquivo = list(fp)
#fp.close()
#print(linhas_do_arquivo)

import pprint
lista_strip = [' ', '.', ',', '/', '\\', '-']

fp = open('memoriaspostumas.txt')
linhas_do_arquivo = list(fp)
#print('Total ' + str(len(linhas_do_arquivo)))
#print(linhas_do_arquivo)
count_void = 0
count_filled = 0
linhas_tratadas_do_arquivo = []
for linha in linhas_do_arquivo:
    linha_tratada = linha
    for caractere in lista_strip:
        linha_tratada = linha_tratada.strip(caractere)
    if linha_tratada != '':
        linhas_tratadas_do_arquivo.append(linha_tratada)
        
# TODO(mcsalgado): lista de palavras em vez de lista de lista de palavras      
# imprimir o numero de ocorrencias para cada palavra
linhas2 = []
count = 0
n_letra = 0
# quebrando em linhas


for linha in linhas_tratadas_do_arquivo:
    # transformando a linha em lista
        linha_quebrada = linha.split()

    # iterando entre as palavras contidas na linha
    for palavra in linha_quebrada:
        # tronando todas as palavras minúsculas
        palavra = palavra.lower()

        linhas2.append(palavra)
        if palavra[0] == 'n':
            count += 1
        for letra in palavra:
            n_letra += 1
#    linhas2.extend(linha_quebrada)

#print(linhas2)
#print(count)
#print(n_letra)

ocorrencia = {}

for palavra in linhas2:
    if palavra in ocorrencia:
        ocorrencia[palavra] += 1
    else:
        ocorrencia[palavra] = 0
        ocorrencia[palavra] = 1

for chave, valor in ocorrencia.items():
    print(str(chave) + '\t\t\t\t\t\t\t' + str(valor))

#pprint.pprint(ocorrencia)
#linhas3 = []
#for linha in linhas_tratadas_do_arquivo:
#    linha_quebrada = linha.split()
#    linhas3.append(linha_quebrada)

#print(linhas3)
