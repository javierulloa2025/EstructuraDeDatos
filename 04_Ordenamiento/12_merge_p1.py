def dividir_lista(lista):
    # Caso base: la lista tiene 0 o 1 elemento
    if len(lista) <= 1:
        return (lista)
    
    # Dividir la lista en dos mitades
    mitad = len(lista) // 2
    izquierda = lista[:mitad]
    print(izquierda)
    derecha = lista[mitad:]
    print(derecha)
    
    izquierda = dividir_lista(izquierda) #recursión
    derecha = dividir_lista(derecha) #recursión
    
li = [8, 10, 4, 2, 1, 7, 6]
print(li)
dividir_lista(li)

