#Busqueda secuencial

def secuencial(lista, buscado):
    posicion = -1
    for i in range(0, len(lista)):
        if (lista[i] == buscado):
            posicion = i
    return posicion
    
l = [4, 5, 6, 7, 8, 9]

encontrado = secuencial(l, 9)
print(encontrado)

