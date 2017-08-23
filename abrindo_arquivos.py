#fp = open('text.txt')
#linhas_do_arquivo = list(fp)
#fp.close()
#print(linhas_do_arquivo)

fp = open('memoriaspostumas.txt')
linhas_do_arquivo = list(fp)
print(len(linhas_do_arquivo))
#print(linhas_do_arquivo)
count_void = 0
count_filled = 0
for linha in linhas_do_arquivo:
    if linha == ' \n' or linha == '\n':
        count_void += 1
    else:
        count_filled += 1

print('Void lines: ' + str(count_void))
print('Filled lines: ' + str(count_filled))
        
