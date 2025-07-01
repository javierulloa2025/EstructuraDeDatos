#Creando una lista de pares a partir de un for
pares = []

for par in range(22):
    if par % 2 == 0:
        pares.append(par)

print(pares)