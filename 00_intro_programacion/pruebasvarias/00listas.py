#llenar la lista con un for
vacia = []
for i in range(10):
    vacia.append(i)
print(vacia)

#llenar la lista con un while
otra_lista = []
x=1
while x < 11:
    otra_lista.append(x)
    x += 1
print(otra_lista)

#lista con pares
pares=[]
for i in range(0,11,2):
    pares.append(i)

print(pares)

#ordenar
pares.sort(reverse=True)
print(pares)

#max y min en lista
print(max(pares))
print(min(pares))

#promedio
promedio = sum(pares)/len(pares)
print(promedio)
