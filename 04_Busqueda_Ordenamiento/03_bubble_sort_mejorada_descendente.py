#Método de ordenamiento burbuja mejorada, descendente
def burbuja(lista):
    cont = 0 #contador para medir iteraciones
    ordenado = False
    n = len(lista)

    for i in range(n - 1):
        if ordenado == True:
            break
        ordenado = True
        for j in range(n-1-i):
            cont += 1
            if lista[j] < lista[j + 1]: #orden descendente
                temp = lista[j]
                lista[j] = lista [j + 1]
                lista[j + 1] = temp
                ordenado=False
    return lista, cont
    
#lista = [20, -19, 5, 6, 15, -4, 0, 18, 7, 3] #42 iteraciones
#lista=[1,2,3,5,4] #10 iteraciones
#lista =[1, 2, 3, 4, 5, 6, 7]  #21 iteraciones porque la lista está totalmente desordenada
lista = [7, 6, 5, 4, 3, 2, 1]  #6 iteraciones porque la lista está descendente

print(lista)
lista_ordenada,cont=burbuja(lista)
print(lista_ordenada,cont)


