#algoritmo para crear una lista random

import random

lista = [random.randint(1, 100) for _ in range(10)]
#Crea una lista de 20 elementos, con elementos random enteros entre 1 y 100
#Utiliza comprensión list 
print(lista)

#Otra opción sin usar listas por comprensión
lista2 = []
for _ in range(10):
    lista2.append(random.randint(1, 100))

print(lista2)