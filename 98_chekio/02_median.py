"""La mediana representa el valor en la posición central de un conjunto de datos ordenados. 
En una lista con un número impar de elementos la mediana se encuentra en la posición central.
Si la lista tiene un número par de elementos, 
no existe un valor central que divida la lista en dos partes iguales 
por lo que la mediana equivale a la media de los dos valores centrales. 
En esta misión, recibirás una lista no vacía de números naturales (X). 
Con ella deberás de separar la parte superior e inferior para encontrar la mediana. """

def checkio(data: list[int]) -> int | float:
    # replace this for solution
    ordena = sorted(data)
    n = len(data)
    punto_medio = n // 2 #indice central 
    if len(ordena) % 2 == 1:
        return ordena[punto_medio]
    else:
        return (ordena[punto_medio-1] + ordena[punto_medio]) / 2

print(checkio([1, 2, 3, 4, 5]))