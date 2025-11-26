class MaxHeap:
    def __init__(self):
        # El heap se almacena en una lista (índice 0 sin usar para facilitar fórmulas)
        self.heap = [None]
        self.size = 0

    # ----------------------------------------------------
    # Funciones auxiliares para índices
    # ----------------------------------------------------
    def padre(self, i):
        return i // 2

    def izquierda(self, i):
        return 2 * i

    def derecha(self, i):
        return 2 * i + 1

    # ----------------------------------------------------
    # Insertar un elemento en el Max-Heap
    # ----------------------------------------------------
    def inserta(self, value):
        self.heap.append(value)
        self.size += 1
        self._recorre_arriba(self.size)

    # Recorrer hacia arriba corrigiendo el heap
    def _recorre_arriba(self, i):
        while i > 1 and self.heap[self.padre(i)] < self.heap[i]:
            # Intercambia con el padre
            self.heap[self.padre(i)], self.heap[i] = self.heap[i], self.heap[self.padre(i)]
            i = self.padre(i)

    # ----------------------------------------------------
    # Obtener el valor máximo sin eliminarlo
    # ----------------------------------------------------
    def obtener_max(self):
        if self.size == 0:
            return None
        return self.heap[1]

    # ----------------------------------------------------
    # Extraer el máximo (root) y reacomodar heap
    # ----------------------------------------------------
    def extraer_max(self):
        if self.size == 0:
            return None

        max_value = self.heap[1]

        # Mover el último elemento a la raíz
        self.heap[1] = self.heap[self.size]
        self.heap.pop()
        self.size -= 1

        # Reacomodar hacia abajo
        self._recorre_abajo(1)

        return max_value

    # Recorre hacia abajo para restaurar la propiedad de Max-Heap
    def _recorre_abajo(self, i):
        while self.izquierda(i) <= self.size:
            # Hijo izquierdo
            max_child = self.izquierda(i)

            # Si existe hijo derecho y es mayor, escoge ese
            if self.derecha(i) <= self.size and self.heap[self.derecha(i)] > self.heap[max_child]:
                max_child = self.derecha(i)

            # Si el padre es mayor que ambos hijos, stop
            if self.heap[i] >= self.heap[max_child]:
                break

            # Intercambia con el hijo mayor
            self.heap[i], self.heap[max_child] = self.heap[max_child], self.heap[i]
            i = max_child

    # ----------------------------------------------------
    # Aumentar el valor de una clave en un índice dado
    # ----------------------------------------------------
    def incrementar_clave(self, index, nuevo_valor):
        if nuevo_valor < self.heap[index]:
            raise ValueError("El nuevo valor debe ser mayor que el actual.")

        self.heap[index] = nuevo_valor
        self._recorre_arriba(index)

    # ----------------------------------------------------
    # Construir heap desde una lista (Heapify)
    # ----------------------------------------------------
    def construye_heap(self, arr):
        self.heap = [None] + arr[:]  # copiar y agregar un None inicial
        self.size = len(arr)

        # Comenzar desde el último nodo no hoja
        for i in range(self.size // 2, 0, -1):
            self._recorre_abajo(i)

    # ----------------------------------------------------
    # Mostrar heap como lista
    # ----------------------------------------------------
    def __str__(self):
        return str(self.heap[1:])  # ignorar índice 0


h = MaxHeap()
lista = [30,17,13,12,11,7,4,6,50,40]

for i in lista:
    h.inserta(i)

print(h)
