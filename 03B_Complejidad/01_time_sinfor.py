""" Una forma diferente de sumar los números de 1 a n usando la fórmula
(n *(n+1)) / 2  """

import time

rango= int(input("¿Hasta cuanto quieres sumar? "))
inicio = time.perf_counter()

total = (rango * (rango + 1)) / 2
print(total)

fin = time.perf_counter()
print(f"Tiempo de ejecución total: {fin - inicio:.6f} segundos")

#Tiempo O(1)