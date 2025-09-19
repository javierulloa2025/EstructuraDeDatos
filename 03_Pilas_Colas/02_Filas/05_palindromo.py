"""Programa que usa las clases Fila y Pila 
para comprobar si una frase o palabra es palíndromo
Ejemplos:
    Reconocer
    Anna
    Ojo rojo
    La ruta nos aportó otro paso natural
"""

from claseFila import Fila
from clasePila import Pila

def es_palindromo(frase):
    #pasamos a minusculas y quitamos espacios
    frase_procesada = frase.lower().replace(" ","")
    #reemplazamos acentos
    frase_procesada = frase_procesada.replace("á","a")
    frase_procesada = frase_procesada.replace("é","e")
    frase_procesada = frase_procesada.replace("í","i")
    frase_procesada = frase_procesada.replace("ó","o")
    frase_procesada = frase_procesada.replace("ú","u")

    #iniciar pila y cola
    pila = Pila()
    fila = Fila()

    #llenamos ambas estructuras
    for caracter in frase_procesada:
        pila.insertar(caracter)
        fila.encolar(caracter)
    
    #Comparamos
    while pila.tamanio() > 0:
        if pila.quitar_elemento() != fila.quitar():
            return False
    return True

#Ejecutamos y probamos
frase = input("Ingresa una frase: ")
if es_palindromo(frase):
    print("Es palindromo")
else:
    print("No es palindromo")