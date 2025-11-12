""" Pruebas varias para eliminar nodo, no le hagas mucho caso a éste código"""
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

    def eliminar_nodo(self, valor):  
        #Caso árbol vacío
        if self.valor is None:    
            return self
        
        #búsqueda recursiva
        if valor < self.valor:   
            if self.izquierdo:
                self.izquierdo = self.izquierdo.eliminar_nodo(valor)
        elif valor > self.valor:
            if self.derecho:
                self.derecho = self.derecho.eliminar_nodo(valor)
        else:
            #Caso 1: sin hijos (nodo hoja)
            if self.izquierdo is None and self.derecho is None:
                return None
            #Caso 2: un hijo
            elif self.izquierdo is None:
                return self.derecho
            elif self.derecho is None:
                return self.izquierdo
            #Caso 3: dos hijos, reemplazo por el mínimo del subarbol derecho
            else:
                sucesor = self.derecho.encontrar_min()
                self.valor = sucesor.valor
                self.derecho = self.derecho.eliminar_nodo(sucesor.valor)
        return self
    
    def encontrar_min(self):
        if self.valor is None:
            return None
        actual = self
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual
    
    def encontrar_max(self):
        if self.valor is None:
            return None
        actual = self
        while actual.derecho:
            actual = actual.derecho
        return actual
        
ar = ArbolBinario(3)
ar.insertar(1)
ar.insertar(4)

maximo = ar.encontrar_max()
if maximo:
    print(maximo.valor)
else:
    print("árbol vacío")
