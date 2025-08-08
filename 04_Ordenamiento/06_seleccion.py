#Método de ordenamiento selección

def seleccion(lista):
    for i in range(0, len(lista)-1):
        minimo = i
        for j in range(i+1, len(lista)):
            if(lista[j] < lista[minimo]):
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return(lista)

l = [222, 33, 14, 23, 11, 78, 9]  #salida [9, 11, 14, 23, 33, 78, 222] 

ordenado = seleccion(l)

print(ordenado)

