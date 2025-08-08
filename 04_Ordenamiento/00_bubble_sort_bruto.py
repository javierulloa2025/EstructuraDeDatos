#Método de ordenamiento burbuja (completo o bruto)
def burbuja(lista):
    n = len(lista)
    contador = 0

    for i in range(0, n-1):
        for j in range(0, n -1):
            contador += 1
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista [j + 1]
                lista[j + 1] = temp
    return lista,contador
    
lista = [20, -19, 5, 6, 15, -4, 0, 18, 7, 3]  # lista ordanada 81 veces (n-1 al cuadrado)

print(lista)
lista_ordenada, cont = burbuja(lista)
print(lista_ordenada,cont) #lista ordanada más contador


