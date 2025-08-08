#Busqueda secuencial con centinela, 
# detiene el ciclo al encontrar

def secuencial(lista, buscado):
    posicion = -1
    for i in range(0, len(lista)):
        if (lista[i] == buscado):
            posicion = i
            break
    return posicion
    
l = [4, 5, 6, 7, 8, 9]

encontrado = secuencial(l, 7)
print(encontrado)



