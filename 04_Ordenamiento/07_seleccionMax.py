#Método de ordenamiento selección

def seleccion(lista):
    for i in range(0, len(lista)-1):
        maximo = i
        for j in range(i+1, len(lista)):
            if(lista[j] > lista[maximo]):
                maximo = j
        lista[i], lista[maximo] = lista[maximo], lista[i]
    return(lista)

l = [222, 33, 14, 23, 11, 78, 9]  #salida [222, 78, 33, 23, 14, 11, 9] 

ordenado = seleccion(l)

print(ordenado)

