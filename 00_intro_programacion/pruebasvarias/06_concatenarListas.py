#Existen varios métodos para concatenar listas

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# 1) Metodo simple +
print(lista1 + lista2)
print(lista1) #no se modificia la lista

# 2) extend()   #Modifica la lista original
lista1.extend(lista2)
print(lista1)

# 3) Unpacking (*) (Python 3.5+)
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
resultado = [*lista1, *lista2]
print(resultado)

# += (similar a extend)
lista1 += lista2
print(lista1) #modificó la lista


