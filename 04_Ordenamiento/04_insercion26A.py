def ordena_insercion(lista):
    for i in range (1, len(lista)):
        valorActual = lista[i]
        posicion = i - 1
        while (posicion>=0) and (lista[posicion] > valorActual):
            lista[posicion + 1] = lista[posicion]
            posicion -= 1
        lista[posicion + 1] = valorActual
    return lista

lista = [9, 8, 7, 6, 5]  
lista_ordenada = ordena_insercion(lista)
print(lista_ordenada)
