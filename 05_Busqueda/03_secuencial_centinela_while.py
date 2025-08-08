#busqueda centinela con while

def seq_cen_while(lista, buscado):
    posicion = -1
    i = 0
    while (i < len(lista)) and (posicion == -1):
        if (lista[i] == buscado):
            posicion = i
        i += 1
    return posicion

l = [4, 5, 6, 7, 8, 9]
encontrado = seq_cen_while(l, 6)
print(encontrado)
