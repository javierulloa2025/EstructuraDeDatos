import random
import time

lista = [random.randint(1, 10000) for _ in range(1000000)]

# Medir tiempo
inicio = time.perf_counter()

lista_temp = lista.copy()

for i in range(len(lista_temp)):
    min_idx = i
    for j in range(i + 1, len(lista_temp)):
        if lista_temp[j] < lista_temp[min_idx]:
            min_idx = j
    lista_temp[i], lista_temp[min_idx] = lista_temp[min_idx], lista_temp[i]

print(lista_temp)
fin = time.perf_counter()
print(f"\nTiempo de ejecución total: {fin - inicio:.6f} segundos")