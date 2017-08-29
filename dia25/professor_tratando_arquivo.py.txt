def dicionário_de_ocorrências(l):
    ret = dict()
    for elemento in l:
        ret[elemento] = 0

    for elemento in l:
        ret[elemento] += 1
    return ret

def ordenado_por_valor(d):
    lista_valor_chave = []
    for chave in list(d):
        lista_valor_chave.append((d[chave], chave))

    ret = sorted(lista_valor_chave, reverse=True)
    return ret

fp = open('memoriaspostumas.txt')
linhas_do_arquivo = list(fp)
fp.close()

# removendo espaços das linhas
linhas_tratadas_do_arquivo = []
for linha in linhas_do_arquivo:
    linha_tratada = linha.strip()
    if linha_tratada != '':
        linhas_tratadas_do_arquivo.append(linha_tratada)

número_de_linhas_não_vazias = len(linhas_tratadas_do_arquivo)
print('Número de linhas não vazias:', número_de_linhas_não_vazias)

# quebrando as linhas em palavras
palavras = []
for linha in linhas_tratadas_do_arquivo:
    linha_quebrada = linha.split()
    for palavra in linha_quebrada:
        palavras.append(palavra)

número_de_palavras = len(palavras)
print('Número de palavras:', número_de_palavras)

# deixando as palavras em minúsculo
palavras_minúsculo = []
for palavra in palavras:
    palavras_minúsculo.append(palavra.lower())

# removendo pontuação das palavras
palavras_sem_pontuação = []
for palavra in palavras_minúsculo:
    palavras_sem_pontuação.append(palavra.strip('.').strip('!').strip(';').strip('?').strip('.').strip(',').strip("'").strip('"').strip('“').strip(':').strip('!').strip('”').strip(')').strip('('))

número_de_palavras_que_começam_com_n = 0
for palavra in palavras_sem_pontuação:
    if palavra.startswith('n'):
#   if palavra[0] == 'n':
        número_de_palavras_que_começam_com_n += 1

print('Número de palavras que começam com n:', número_de_palavras_que_começam_com_n)
print()

ocorrências = dicionário_de_ocorrências(palavras_sem_pontuação)
lista_de_ocorrencias_palavras = ordenado_por_valor(ocorrências)

print('TOP PALAVRAS')
for elemento in lista_de_ocorrencias_palavras[0:10]:
    print(elemento)
print()

# cria uma lista de bigrams
bigrams = []
palavra_anterior = ''
for palavra in palavras_sem_pontuação:
    bigram = (palavra_anterior, palavra)
    bigrams.append(bigram)
    palavra_anterior = palavra

ocorrências_bigrams = dicionário_de_ocorrências(bigrams)
lista_de_ocorrencias_bigrams = ordenado_por_valor(ocorrências_bigrams)

print('TOP BIGRAMS')
for elemento in lista_de_ocorrencias_bigrams[0:10]:
    print(elemento[1], (elemento[0]/len(bigrams))*100)
print()

# cria uma lista de trigrams
trigrams = []
palavra_anterior = ''
palavra_anterior_anterior = ''
for palavra in palavras_sem_pontuação:
    trigram = (palavra_anterior_anterior, palavra_anterior, palavra)
    trigrams.append(trigram)
    palavra_anterior_anterior = palavra_anterior
    palavra_anterior = palavra

ocorrências_trigrams = dicionário_de_ocorrências(trigrams)
lista_de_ocorrencias_trigrams = ordenado_por_valor(ocorrências_trigrams)

print('TOP TRIGRAMS')
for elemento in lista_de_ocorrencias_trigrams[0:10]:
    print(elemento[1], (elemento[0]/len(trigrams))*100)
