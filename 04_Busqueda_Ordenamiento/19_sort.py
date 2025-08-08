""" Método .sort() ordena solo listas no aplica con otros iterables"""
listanumero = [15, 2, 6, 12, 9, 0]
listanumero.sort()
print(listanumero)

cadena = "hola"
# cadena.sort() #str no tiene un método sort 
print(sorted(cadena)) #salida ['a', 'h', 'l', 'o']