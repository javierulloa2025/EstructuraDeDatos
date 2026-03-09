class Nodo:
    def __init__(self, info=None):
        self.info = info
        self.sig = None
        self.id = None

# Lista vacía al inicio
cabeza = None
cola = None
contador_id = 1  # próximo id a asignar
total_nodos = 0  # contador real de nodos creados

palabra = input("Ingresa una palabra o Enter vacío para terminar: ")

while palabra != "":
    nuevo = Nodo(palabra)
    nuevo.id = contador_id     # Asignar el id al nodo
    contador_id += 1           # Preparar el siguiente id
    total_nodos += 1           # Llevar conteo de nodos creados

    if cabeza is None:
        # Primer nodo
        cabeza = nuevo
        cola = nuevo
    else:
        # Insertar al final
        cola.sig = nuevo
        cola = nuevo

    palabra = input("Ingresa otra palabra o Enter vacío para terminar: ")

print("\nLista completa:")
actual = cabeza
while actual is not None:
    print(f"Nodo ID {actual.id} - Valor: {actual.info}")
    actual = actual.sig

print(f"\nTotal de nodos: {total_nodos}")