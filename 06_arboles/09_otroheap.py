class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def padre(self,indice):
        return(indice-1) // 2
    
    def hijo_izquierdo(self, indice):
        return 2*indice + 1
    
    def hijo_derecho(self, indice):
        return 2*indice + 2
    
    def insertar(self, valor):
        self.heap.append(valor)
        self.recorre_arriba(len(self.heap)-1)

    def recorre_arriba(self,indice):
        while indice != 0 and self.heap[self.padre(indice)] < self.heap[indice]:
            self.heap[self.padre(indice)], self.heap[indice] = self.heap[indice], self.heap[self.padre(indice)]

            indice = self.padre(indice)
    
    def extraer_max(self):
        if not self.heap:
            return None
        
        maximo = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.recorre_abajo(0)
        return maximo
    
    def recorre_abajo(self, indice):
        tamanio = len(self.heap)
        masgrande = indice 

        while True:
            izquierdo = self.hijo_izquierdo(indice)
            derecho = self.hijo_derecho(indice)

            if izquierdo < tamanio and self.heap[izquierdo] > self.heap[masgrande]:
                masgrande = izquierdo
            if derecho < tamanio and self.heap[derecho] > self.heap[masgrande]:
                masgrande = derecho
            if masgrande != indice:
                self.heap[indice], self.heap[masgrande] = self.heap[masgrande], self.heap[indice]
                indice = masgrande
            else:
                break

    def construye_maxHeap(self, lista):
        self.heap = lista[:]
        for i in range(len(self.heap)//2- 1, -1, -1):
            self.recorre_abajo(i)

    def __str__(self):
        return str(self.heap[:])
    
h = MaxHeap()
h.insertar(8)
h.insertar(2)
h.insertar(5)
h.insertar(12)
h.insertar(1)
print(h)
print(h.extraer_max())
print(h)

lista1 = [90, 80 , 20 , 10 , 20]
h2 = MaxHeap()
h2.construye_maxHeap(lista1)
print(h2)
        