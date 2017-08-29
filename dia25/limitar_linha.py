s = 'Chaves é uma pessoa interessate, uma vez eu vi o Chaves em Acapulco. '
texto = s*10

texto_a_imprimir = ''
for i, letra in enumerate(texto):
    if i % 30 == 0:
        texto_a_imprimir += '\n'
    texto_a_imprimir += letra

print(texto_a_imprimir)
