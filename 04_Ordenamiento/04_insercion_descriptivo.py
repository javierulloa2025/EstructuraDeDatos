def ordena_insercion(lista):
    cambios=0
    print(lista)
    for i in range (1, len(lista)+1):  #no tiene sentido empezar a comparar el elemento 0
        k=i-1
        while (k>0) and (lista[k] < lista[k-1]):
            print(f"Tomamos el {lista[k]}")
            print(f"{lista[k]} es menor que {lista[k-1]}, los cambiamos")
            lista[k], lista[k-1] = lista[k-1], lista[k]
            print(lista)
            k -= 1
            cambios+=1
    return lista,cambios

lista = [9, 8, 7, 6, 5]  # 10 cambios
#lista = [1, 2, 3, 4, 5, 6, 7] # 0 cambios
#lista = [9, 8 , 7, 6, 5, 4, 3, 2, 1] # 36 cambios
lista_ordenada, cambios = ordena_insercion(lista)
print(f"Lista ordenada: {lista_ordenada}, cambios: {cambios}")
