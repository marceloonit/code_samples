nomes = ['Ana', 'Beto', 'Carla', 'Daniel', 'Eduardo']

#TOSCO 1
i = 0
for nome in nomes:
    print(i, nome)
    i += 1

print()

#TOSCO 2
for i in range(len(nomes)):
    print(i, nomes[i])
    
print()
    
#LEGAL
for i, nome in enumerate(nomes):
    print(i, nome)
