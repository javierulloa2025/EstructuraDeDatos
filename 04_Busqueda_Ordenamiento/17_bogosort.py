import random

def is_sorted(arr):
    """Verifica si la lista está ordenada."""
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def bogo_sort(arr):
    """Ordena la lista revocando aleatoriamente hasta que esté ordenada."""
    attempts = 0
    while not is_sorted(arr):
        random.shuffle(arr)
        attempts += 1
        print(f"Intento {attempts}: {arr}")  # Opcional: ver los intentos
    return arr

# Ejemplo de uso
lista = [3, 1, 2]
print("Lista original:", lista)
lista_ordenada = bogo_sort(lista.copy())  # Usamos copy() para no modificar la original
print("\nLista ordenada:", lista_ordenada)