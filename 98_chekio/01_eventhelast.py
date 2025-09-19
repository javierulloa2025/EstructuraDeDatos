""" Se te da un arreglo de enteros. 
Deberías encontrar la suma de los elementos con índices pares (0, 2do, 4to... ) 
luego multiplicar ese resultado con el elmento final del arreglo. 
No olvides que el primer elemento tiene el índice 0.

Para un arreglo vacio, el resultado siempre será 0 (cero). """

def checkio(array: list[int]) -> int:
    # your code here
    lista_pares=[]
    suma = 0
    if len(array) <= 0:
        return 0         
    else:
        for indice, valor in enumerate(array):
            if indice % 2 == 0:
                lista_pares.append(valor)
            suma = sum(lista_pares)
    return suma * array[-1]
    
    

print("Example:")
print(checkio([1, 3, 5])) # salida 30