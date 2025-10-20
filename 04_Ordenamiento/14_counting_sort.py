def counting_sort(lista, maximo=9):
    """Método de ordenamiento countsort"""
    maximo = max(l)
    lista_conteo = [0] * (maximo + 1) #creamos la lista de conteo (+1 por indice 0)
    lista_ordenada = [None] * len(lista) #creamos una lista ordenada vacía de momento

    for i in lista:
        lista_conteo[i] += 1  #cuenta la frecuencia de números en la lista

    total = 0   
    for i in range(len(lista_conteo)):  
        lista_conteo[i], total = total, total + lista_conteo[i]  #frecuenta acumulada

    for indice in lista:
        lista_ordenada[lista_conteo[indice]] = indice  #ordena los números
        lista_conteo[indice] += 1   
    return lista_ordenada

l = [0, 3, 9, 1, 8, 5, 3, 2, 2,10]
r = counting_sort(l)
print(r)
