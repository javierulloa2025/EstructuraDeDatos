#Método de ordenamiento burbuja mejorada
def burbuja(lista):
    cont = 0 #contador para medir iteraciones
    ordenado = False
    n = len(lista)

    for i in range(0, n-1):
        if ordenado == True:
            break
        for j in range(0, n -i -1):
            ordenado=True
            cont += 1
            if lista[j] > lista[j + 1]:
                ordenado=False
                temp = lista[j]
                lista[j] = lista [j + 1]
                lista[j + 1] = temp
    return lista, cont
    
#lista = [20, -19, 5, 6, 15, -4, 0, 18, 7, 3] #45 veces sin burbuja normal, 42 burbuja ordenada
#lista=[1,2,3,5,4] #10 veces sin mejorada y 7 mejorada
lista =[1, 2, 3, 4, 5, 6, 7]  #6 iteraciones (n-1) mejorada, 21 sin mejorar (mejor caso porque la lista está ordenada)

print(lista)
lista_ordenada,cont=burbuja(lista)
print(lista_ordenada,cont)


