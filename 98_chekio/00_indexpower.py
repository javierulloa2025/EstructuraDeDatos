""" Se te da un arreglo con números positivos y un número N. 
Deberías encontrar la N-ésima potencia del elemento en el arreglo con el índice N. 
Si el indíce N está afuera del arreglo, entonces devolver -1. 
No olvides que el primer elemento tene el índice 0.

Miremos algunos ejemplos:
- arreglo = [1, 2, 3, 4] y N = 2, entonces el resultado es 32 == 9;
- arreglo = [1, 2, 3] y N = 3, pero N está afuera del arrego, entonces el resultado es -1. """

def index_power(ar: list[int], n: int) -> int:
    if n >= len(ar):
        return -1
    else:
        return ar[n] ** n


print("Example:")
print(index_power([96, 92, 94], 3))