from functools import lru_cache   #Visto en https://www.youtube.com/shorts/-rRQpvAd9YQ 
import time

hasta = int(input("¿Hasta qué número?: "))
# Medición del tiempo
inicio = time.perf_counter()

#Sucesión de Fibonacci con recursividad
@lru_cache  #Cache que optimiza el tiempo
def fib(n):
    if n == 0 or n == 1:  #Caso base
        return n
    else:
        return fib(n-1) + fib(n-2)
    
for numero in range(0, hasta):
    print(f"{fib(numero)}", end=" ")

fin = time.perf_counter()
print(f"Tiempo de ejecución total: {fin - inicio:.4f} segundos")

