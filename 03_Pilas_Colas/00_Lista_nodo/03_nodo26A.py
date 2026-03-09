class Nodo:
    def __init__(self, info=None):
        self.info = info
        self.sig = None

# Lista vacía al inicio
cabeza = None
cola = None

palabra = input("Ingresa una palabra o Enter vacío para terminar: ")

while palabra != "":
    nuevo = Nodo(palabra)
    if cabeza is None:
        # Primer nodo
        cabeza = nuevo
        cola = nuevo
    else:
        # Insertar al final
        cola.sig = nuevo
        cola = nuevo
    palabra = input("Ingresa otra palabra o Enter vacío para terminar: ")

print("Lista completa:")
actual = cabeza
while actual is not None:
    print(actual.info)
    actual = actual.sig
