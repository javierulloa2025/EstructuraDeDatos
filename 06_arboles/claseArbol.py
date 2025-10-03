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

#Mostrar como lista de elementos ordenados
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

#Altura
    def altura_arbol(self):
        
        altura_izq = self.izquierdo.altura_arbol() if self.izquierdo else -1
        altura_der = self.derecho.altura_arbol() if self.derecho else -1

        return max(altura_der, altura_izq) + 1

#Buscar valores (True / False)
    def buscar(self,valor):
        if self.valor is None:
            return False
        
        if valor == self.valor:
            return True
        elif valor < self.valor and self.izquierdo:
            return self.izquierdo.buscar(valor)
        elif valor > self.valor and self.derecho:
            return self.derecho.buscar(valor)
        else:
            return False
        
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
    
    def encontrar_max(self):
        actual = self
        while actual.derecho:
            actual = actual.derecho
        return actual



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