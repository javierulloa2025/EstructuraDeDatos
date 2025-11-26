from clase_heap import MaxHeap

def heap_sort(lista):
    h = MaxHeap()
    h.construye_maxHeap(lista)
    resultado = []

    while len(h.heap) > 0:
        resultado.append(h.extraer_max())

    return resultado[::-1]



#Ejemplo de uso
lista = [30,17,13,12,11,7,4,6,50,40]
ordenada = heap_sort(lista)
print("Lista original:", lista)
print("Lista ordenada:", ordenada)
