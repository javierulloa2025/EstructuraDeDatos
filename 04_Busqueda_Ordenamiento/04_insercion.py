def ordena_insercion(lista):
    iteraciones = 0
    cambios=0
    for i in range (1, len(lista)+1):
        iteraciones += 1
        k=i-1
        while (k>0) and (lista[k] < lista[k-1]):
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k -= 1
            cambios+=1
    return lista,iteraciones,cambios

#lista = [9, 8, 7, 6, 5]  #5 iteraciones , 10 cambios
#lista = [1, 2, 3, 4, 5, 6, 7] #7 iteraciones, 0 cambios
lista = [9, 8 , 7, 6, 5, 4, 3, 2, 1]
lista_ordenada, contador,cambios = ordena_insercion(lista)
print(lista_ordenada, contador, cambios)
