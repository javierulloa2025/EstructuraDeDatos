cadena = "Francisco Javier Ulloa Áraiza"
cadena.lower()

def cuenta_vocales(cadena):
    contador = 0
    vocales = {"a","e","i","o","u","á","é","í","ó","ú"}
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

print(cuenta_vocales(cadena))
#Salida esperada: 10