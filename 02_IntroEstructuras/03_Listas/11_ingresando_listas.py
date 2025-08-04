""" Crea dos arreglos de la misma longitud, solicita por teclado los nombres que se almacenan en la primer lista
En la segunda lista se almacena la longitud de cada uno de los nombres.
"""
nombres = []
longitudes = []
tamanio = int(input("Ingresa el tamaño de las listas: "))

for i in range(tamanio):
    nombres.append(input("Ingresa el nombre: "))
    longitudes.append(len(nombres[i]))

for x in range(tamanio):
    print(f"{nombres[x]} tiene {longitudes[x]} letras")
    

#Iterar sobre múltiples listas (usando la función zip)

for nombre, longitud in zip(nombres,longitudes):
    print(f"{nombre} tiene {longitud} letras")