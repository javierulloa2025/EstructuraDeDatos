def binariar(lista, x):
    if len(lista) <= 0:
        return ("Lista vacia o número no encontrado")
    
    medio = lista[len(lista) // 2]
    if medio == x:
        return ("Número encontrado")
    else:
        if x < medio:
            return binariar(lista[:len(lista) // 2], x)
        else:
            return binariar(lista[(len(lista) //2) + 1:], x)

        
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(binariar(lista, 15))