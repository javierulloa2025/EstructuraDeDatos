import random
import time

tamanio = int(input("¿Cuántos elementos en la lista?: "))
lista_aleatoria = [random.randint(1, 1000) for _ in range(tamanio)]
print(f"Lista aleatoria: {lista_aleatoria}")
inicio = time.perf_counter()

#Método de ordenamiento selección
def seleccion(lista):
    for i in range(0, len(lista)-1):
        maximo = i
        for j in range(i+1, len(lista)):
            if(lista[j] > lista[maximo]):
                maximo = j
        lista[i], lista[maximo] = lista[maximo], lista[i]
    return(lista)

lista_ordenada = seleccion(lista_aleatoria)
print(f"Lista ordenada: {lista_ordenada}")

fin = time.perf_counter()
print(f"Tiempo de ejecución total: {fin - inicio:.4f} segundos")
 



