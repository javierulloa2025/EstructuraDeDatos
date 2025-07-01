lista_num = [3, 4, 56, 7, 1, 0, -3]

#Orden ascendente (por defecto)
lista_num.sort()
print(lista_num)

#Orden descendente
lista_num.sort(reverse=True)
print(lista_num)

#usando en lugar sorted, devuelve una nueva lista sin afectar la original
ordenados = sorted(lista_num)
print(ordenados)
