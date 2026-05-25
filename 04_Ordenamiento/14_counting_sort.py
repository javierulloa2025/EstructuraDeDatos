import random
import time

def counting_sort(lista, maximo=9):
    """Método de ordenamiento countsort"""
    maximo = max(lista_aleatoria)
    lista_conteo = [0] * (maximo + 1) #creamos la lista de conteo (+1 por indice 0)
    lista_ordenada = [None] * len(lista) #creamos una lista ordenada vacía de momento

    for i in lista:
        lista_conteo[i] += 1  #cuenta la frecuencia de números en la lista

    total = 0   
    for i in range(len(lista_conteo)):  
        lista_conteo[i], total = total, total + lista_conteo[i]  #frecuenta acumulada

    for indice in lista:
        lista_ordenada[lista_conteo[indice]] = indice  #ordena los números
        lista_conteo[indice] += 1   
    return lista_ordenada

#l = [0, 3, 9, 1, 8, 5, 3, 2, 2,10]
tamanio = int(input("¿Cuántos elementos en la lista? (random del 0 al 100): "))
lista_aleatoria = [random.randint(0, 100) for _ in range(tamanio)]

#Medir tiempo
inicio = time.perf_counter()
print(lista_aleatoria)
r = counting_sort(lista_aleatoria)
print(r)
fin = time.perf_counter()
print(f"\nTiempo de ejecución total: {fin - inicio:.6f} segundos")
