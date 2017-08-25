#!usr/bin/env python3

fp = open('memoriaspostumas.txt')
linhas_do_arquivo = list(fp)
fp.close()

# removendo espaços das linhas
linhas_tratadas_do_arquivo = []
for linha in linhas_do_arquivo:
    linha_tratada = linha.strip()
    if linha_tratada != '':
        linhas_tratadas_do_arquivo.append(linha_tratada)

# quebrando as linhas em palavras
palavras = []
for linha in linhas_tratadas_do_arquivo:
    linha_quebrada = linha.split()
    for palavra in linha_quebrada:
        palavras.append(palavra)


set_palavras = set(palavras)

print('O livro tem,', len(palavras), 'palavras, das quais', len(set_palavras), 'são únicas.')
