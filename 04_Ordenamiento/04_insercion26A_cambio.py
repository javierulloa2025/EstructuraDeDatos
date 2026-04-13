def ordena_insercion(lista):
    intercambios=0
    for i in range (1, len(lista)):
        valorActual = lista[i]
        posicion = i - 1
        while (posicion>=0) and (lista[posicion] > valorActual):
            lista[posicion + 1] = lista[posicion]
            intercambios += 1
            posicion -= 1
        lista[posicion + 1] = valorActual
    return lista, intercambios

#lista = [1,2,3,4,5]  #intercambios 0
#lista = [9,8,7,6,5]   #intercambios 10
lista = [9,8,7,6,5,4,3,2,1] #intercambios 36
lista_ordenada, intercambios = ordena_insercion(lista)
print(lista_ordenada)
print(f"Intercambios realizados: {intercambios}")

