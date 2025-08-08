def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mitad = len(lista) // 2
        izquierda = merge_sort(lista[:mitad]) #recursiva
        derecha = merge_sort(lista[mitad:])   #recursiva
    return merge(izquierda, derecha) #llama a función mezcla

def merge(izquierda, derecha):
    #Función para mezclar listas
    resultado = []
    i = j = 0
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1  
    
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

l = [11, 4, 2, 33, 412, 22, 1]
r = merge_sort(l)
print(r)  # Salida: [1, 2, 4, 11, 22, 33, 412]


