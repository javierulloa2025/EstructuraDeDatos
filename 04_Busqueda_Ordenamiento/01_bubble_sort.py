#Método de ordenamiento burbuja
def burbuja(lista):
    n = len(lista)

    for i in range(0, n-1):
        for j in range(0, n -i -1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista [j + 1]
                lista[j + 1] = temp
    return lista
    
lista = [20, -19, 5, 6, 15, -4, 0, 18, 7, 3]

print(lista)
print (burbuja(lista))


