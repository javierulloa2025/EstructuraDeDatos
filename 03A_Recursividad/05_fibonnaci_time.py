import time

# Medición del tiempo
inicio = time.perf_counter()

#Sucesión de Fibonacci con recursividad
def fib(n):
    if n == 0 or n == 1:  #Caso base
        return n
    else:
        return fib(n-1) + fib(n-2)
    
for numero in range(0, 8):
    print(f"{fib(numero)}", end=" ")

fin = time.perf_counter()
print(f"\nTiempo de ejecución total: {fin - inicio:.6f} segundos")

#38: 8.24 segundos
#39: 19.64 segundos