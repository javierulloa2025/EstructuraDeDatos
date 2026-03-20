import time

rango= int(input("¿Hasta cuanto quieres sumar? "))
inicio = time.perf_counter()

total = 0
for num in range(rango):
    total += num
print(total)

fin = time.perf_counter()
print(f"Tiempo de ejecución total: {fin - inicio:.6f} segundos")


#Prueba con 1 millon, luego 2 millones, 3 millones
#Complejidad O(n)
