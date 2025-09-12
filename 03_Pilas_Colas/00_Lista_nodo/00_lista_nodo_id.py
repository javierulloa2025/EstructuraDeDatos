class Nodo(object):
    """Clase nodo simplemente enlazado"""
    info, sig, id = None, None, None

# Contador global para IDs consecutivos
contador_id = 1

# Crear el primer nodo
cabeza = Nodo()
cabeza.info = "Primer nodo"
cabeza.id = contador_id
contador_id += 1

# Crear lista enlazada
palabra = input("Ingrese una palabra, o Enter vacío para terminar: ")
actual = cabeza  # actual apunta al último nodo
while palabra != "":
    nuevo_nodo = Nodo()  # Crea un nuevo nodo
    nuevo_nodo.info = palabra  # Asigna la palabra
    nuevo_nodo.id = contador_id  # Asigna ID consecutivo
    contador_id += 1  # Incrementa el contador
    
    actual.sig = nuevo_nodo  # Enlaza con el anterior
    actual = nuevo_nodo  # Actualiza el último nodo
    palabra = input("Ingrese otra palabra: ")

# Recorrer e imprimir con IDs
print("\nLista completa con IDs: ")
actual = cabeza  # Volvemos al inicio para recorrer
while actual is not None:
    print(f"Nodo ID: {actual.id} - Valor: {actual.info}")
    actual = actual.sig

# Mostrar estadísticas
print(f"\nTotal de nodos en la lista: {contador_id - 1}")