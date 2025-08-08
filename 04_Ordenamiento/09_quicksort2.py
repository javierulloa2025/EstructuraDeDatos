#Algoritmo quicksort más claro
def quicksort2(lista):
    if len(lista) <= 1:   #Caso base [] o len=1
        return(lista)
    else:
        pivote = lista[len(lista) // 2] #elige el elemento central de la lista

        lista_izquierda = []  #almacenará elementos menores al pivote
        lista_derecha = []  # lo mismo pero para mayores al pivote
        lista_centro = []  #se crea por si hay pivotes repetidos

        #Separar elementos
        for elemento in lista:
            if elemento < pivote:   #si es menor del pivote, a la izquierda
                lista_izquierda.append(elemento)
            elif elemento == pivote: #si hay repetidos, al centro
                lista_centro.append(elemento)
            else:
                lista_derecha.append(elemento) #los demás (mayores) a la derecha
    return quicksort2(lista_izquierda) + lista_centro + quicksort2(lista_derecha) #recursividad

desorden = [99, 2, 3, 21, 23, 1, 3]
orden = quicksort2(desorden)
print(orden)




