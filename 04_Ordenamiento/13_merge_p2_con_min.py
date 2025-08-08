def ordena_con_min(l1, l2):
    lr = l1 + l2
    resultado = []
    while len(lr) > 0:
        menor = min(lr)
        resultado.append(menor)
        lr.remove(menor)
    
    return resultado

lista1 = [3, 2, 4, 44, 41]
lista2 = [5, 6, 2, 3, 4, 44, 41]

j = ordena_con_min(lista1, lista2)
print(j) 

