from ClasePila import Pila

mipila = Pila()

print(mipila.vacia())
mipila.insertar("Uno")
mipila.insertar("Dos")
mipila.insertar("Tres")
mipila.insertar("Cuatro")
print(mipila.cima())
mipila.quitar_elemento()
print(mipila.mostrar_elementos())
print(mipila.tamano())
