def dividir_lista(l):
    
    # Caso base: la lista tiene 0 o 1 elemento
    if len(l) <= 1:
        return (l)
    
    # Dividir la lista en dos mitades
    mitad = len(l) // 2
    izquierda = l[:mitad]
    print(izquierda)
    derecha = l[mitad:]
    print(derecha)
    
    izquierda = dividir_lista(izquierda)
    derecha = dividir_lista(derecha)
    
l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
dividir_lista(l)

