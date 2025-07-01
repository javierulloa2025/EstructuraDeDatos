from clasePila import Pila

def invertir_lista(lista):
    p = Pila()
    for elemento in lista:
        p.insertar(elemento)
        
    lista_invertida = []
    while not p.esta_vacia():
        lista_invertida.append(p.quitar_elemento())

    return lista_invertida

print(invertir_lista([1, 2, 3, 4]))  # Salida [4, 3, 2, 1]
print(invertir_lista(["a","b","c","d"])) #Salida ["d","c","b","a"]



