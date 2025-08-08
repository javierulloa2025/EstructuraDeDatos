#Búsqueda binaria (sobre una lista ORDENADA)
def bbinaria(lista, buscado):
    posicion = -1
    primero = 0
    ultimo = len(lista)-1
    while (primero <= ultimo) and (posicion ==-1):
        medio = (primero + ultimo) // 2
        if (lista[medio] == buscado):
            posicion = medio
        else: 
            if (buscado < lista[medio]):
                ultimo = medio - 1
            else:
                primero = medio + 1
    return posicion

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(bbinaria(l, 4))  #salida (posición 3)
print(bbinaria(l,14))  #salida -1 (no encontrado)
