from clasePila import Pila

pil = Pila()

pil.insertar("uno")
pil.insertar("dos")
pil.insertar("tres")
pil.insertar("cuatro")
pil.insertar("cinco")

print(pil.mostrar_elementos())

while (not pil.esta_vacia()):
    print(pil.quitar_elemento())

