def combina_listas(R, L):
    # Función para ordenar una lista (implementación de Bubble Sort)
    def ordenar_lista(lista):
        n = len(lista)
        for i in range(n):
            for j in range(0, n-i-1):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista
    
    # Ordenamos ambas listas
    R_ordenada = ordenar_lista(R.copy())
    L_ordenada = ordenar_lista(L.copy())
    
    combinada = []
    i = j = 0
    
    # Combinamos las listas ordenadas
    while i < len(R_ordenada) and j < len(L_ordenada):
        if R_ordenada[i] <= L_ordenada[j]:
            combinada.append(R_ordenada[i])
            i += 1
        else:
            combinada.append(L_ordenada[j])
            j += 1
    
    # Añadimos los elementos restantes
    combinada += R_ordenada[i:]
    combinada += L_ordenada[j:]
    
    return combinada

R = [3, 2, 4]
L = [4, 2, 3]

resultado = combina_listas(R, L)
print(resultado)  # Output: [2, 2, 3, 3, 4, 4]

print(resultado)