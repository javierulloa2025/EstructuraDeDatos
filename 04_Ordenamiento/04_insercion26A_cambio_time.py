import time
import random

tamanio = int(input("¿Cuántos elementos en la lista?: "))
lista_aleatoria = [random.randint(1, 1000) for _ in range(tamanio)]
print(f"Lista aleatoria: {lista_aleatoria}")
inicio = time.perf_counter()

def ordena_insercion(lista):
    intercambios=0
    for i in range (1, len(lista)):
        valorActual = lista[i]
        posicion = i - 1
        while (posicion>=0) and (lista[posicion] > valorActual):
            lista[posicion + 1] = lista[posicion]
            intercambios += 1
            posicion -= 1
        lista[posicion + 1] = valorActual
    return lista, intercambios

lista_ordenada, intercambios = ordena_insercion(lista_aleatoria)
print(lista_ordenada)
print(f"Intercambios realizados: {intercambios}")
fin = time.perf_counter()
print(f"Tiempo de ejecución: {fin - inicio} segundos")
