"""Calcula la media de un conjunto de 
calificaciones utiliza centinela -99 para el fin del bucle
"""

#Variables inicializadas
total = 0
contador = 0

#Prime valor fuera del bucle
calificacion = float(input ("Escribe la calificación o -99 para salir: "))

while calificacion != -99:
    total += calificacion
    contador += 1

    #pedir la siguiente o -99 para terminar
    calificacion =float(input("Ingresa otra calificación o -99 para salir: "))

if contador > 0:
    media = total / contador
    print(f"La media de las {contador} calificaciones es {media}")
else:
    print("No se ingresaron calificaciones")




