from collections import deque

class ArbolBinario:
    def __init__(self, valor = None):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
    
    def insertar(self, valor):
        #Caso el nodo aún está vacío
        if self.valor is None:
            self.valor = valor
            return

        if valor < self.valor:
            if self.izquierdo is None:
                self.izquierdo = ArbolBinario(valor)
            else:
                self.izquierdo.insertar(valor)
        else:
            if self.derecho is None:
                self.derecho = ArbolBinario(valor)
            else:
                self.derecho.insertar(valor)

    def bfs(self):
        if self.valor is None:
            return []
        
        cola = deque()
        resultado = []

        cola.append(self)

        while cola:
            nodo = cola.popleft()
            resultado.append(nodo.valor)

            if nodo.izquierdo:
                cola.append(nodo.izquierdo)
            if nodo.derecho:
                cola.append(nodo.derecho)

        return resultado

    def mostrar_arbol(self, nivel=0, prefijo="Raíz: "):
        resultado = "    " * nivel + prefijo + str(self.valor) + "\n"
        if self.izquierdo:
            resultado += self.izquierdo.mostrar_arbol(nivel + 1, "Izq: ")
        if self.derecho:
            resultado += self.derecho.mostrar_arbol(nivel + 1, "Der: ")
        return resultado  
    
ar = ArbolBinario(5)
ar.insertar(2)
ar.insertar(7)
ar.insertar(9)
ar.insertar(1)
ar.insertar(4)
print(ar.mostrar_arbol())
print(ar.bfs())