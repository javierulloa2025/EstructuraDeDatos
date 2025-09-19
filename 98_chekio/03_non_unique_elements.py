"""Se te dará una lista no vacía de enteros (X). 
Para esta misión, deberás retornar una lista que consista únicamente de elementos no únicos. 
Para hacerlo, necesitarás eliminar todos los elementos que sean únicos 
(elementos que aparezcan una sola vez en la lista dada). 
Al resolver esta misión, no cambies el orden de la lista. 
Ejemplo: [1, 2, 3, 1, 3] 1 y 3 no son elementos únicos y el resultado será [1, 3, 1, 3]. """

from collections.abc import Iterable
from collections import Counter


def checkio(data: list[int]) -> Iterable[int]:
    # your code here
    contador = Counter(data)
    return [elemento for elemento in data if contador[elemento] > 1]


print(list(checkio([1, 2, 3, 1, 3])))  # salida = [1, 3, 1, 3]