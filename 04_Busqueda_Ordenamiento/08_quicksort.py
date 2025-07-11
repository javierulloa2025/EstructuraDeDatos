#Algoritmo ordanamiento rápido
def quicksort(lista, primero=0, ultimo=None):  #argumento por defecto para primero
    if ultimo is None:   #si no se especifica el ultimo entonces:
        ultimo = len(lista) - 1   
    if primero < ultimo:
        pivote = particion(lista, primero, ultimo)
        quicksort(lista, primero, pivote-1)
        quicksort(lista, pivote+1, ultimo)

def particion(lista, primero, ultimo):
    pivote = lista[ultimo] #selecciona como pivote al ultimo elemento
    i = primero - 1  #apuntador del último elemento más pequeño
    
    for j in range(primero, ultimo):
        if lista[j] <= pivote:
            i += 1  #Avanzar apuntador
            lista[i], lista[j] = lista[j], lista[i]  #intercambio
    #intercambio de pivote
    lista[i+1], lista[ultimo] = lista[ultimo], lista[i+1]
    return i + 1  #regresa la posición final del pivote


# Ejemplo de uso
l = [-1, 33, 44, 55, 2, 6, 78, 2, 99]
print(f"Lista sin ordenar: {l}")
quicksort(l)  
print(f"Lista ordenada: {l}")


