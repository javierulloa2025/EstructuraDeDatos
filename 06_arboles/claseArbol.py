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
        if self is None:
            return None
        
        if valor < self.valor:
            if self.izquierdo:
                self.izquierdo = self.izquierdo.eliminar_nodo(valor)
        elif valor > self.valor:
            if self.derecho:
                self.derecho = self.derecho.eliminar_nodo(valor)
        else:
            #Caso 1: sin hijos
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
        actual = self
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual

    def localizar_elem(self,valor):
        if self.valor is None:
            return False
        
        if valor == self.valor:
            return True
        elif valor < self.valor and self.izquierdo:
            return self.izquierdo.localizar_elem(valor)
        elif valor > self.valor and self.derecho:
            return self.derecho.localizar_elem(valor)
        else:
            return False

    def mostrar_en_orden(self):
        elementos = []
        if self.izquierdo:
            elementos.extend(self.izquierdo.mostrar_en_orden())
        elementos.append(self.valor)
        if self.derecho:
            elementos.extend(self.derecho.mostrar_en_orden())
        return elementos

#Mostrar en forma visual
    def mostrar_arbol(self, nivel=0, prefijo="Raíz: "):
        resultado = "    " * nivel + prefijo + str(self.valor) + "\n"
        if self.izquierdo:
            resultado += self.izquierdo.mostrar_arbol(nivel + 1, "Izq: ")
        if self.derecho:
            resultado += self.derecho.mostrar_arbol(nivel + 1, "Der: ")
        return resultado
    
#Recorridos 
    def preorden(self):
        print(self.valor, end=", ")  #visitar raíz
        if self.izquierdo:
            self.izquierdo.preorden()
        if self.derecho:
            self.derecho.preorden()

    def inorden(self):
        if self.izquierdo:
            self.izquierdo.inorden()
        print(self.valor, end= ", ") #visitar raíz
        if self.derecho:
            self.derecho.inorden()
    
    def postorden(self):
        if self.izquierdo:
            self.izquierdo.postorden()
        if self.derecho:
            self.derecho.postorden()
        print(self.valor, end= ", ")  