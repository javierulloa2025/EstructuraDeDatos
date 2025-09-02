"""encontrar el valor máximo de una lista y pasarlo como parámetro de una función"""

def recorre_lista(l, max):
    for i in range(0, len(l)):
        print(l[i], end=" ")

lista = [1, 2, 3, 5, 6, 3, 4, 9, 9, 1, 8, 7]


recorre_lista(lista, max(lista))