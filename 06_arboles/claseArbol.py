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
        
arbol = ArbolBinario()
valores = [9, 2, 1, 16, 6, 11, 8, 4]
for valor in valores:
    arbol.insertar(valor)

#print(arbol.mostrar_en_orden())
#print(arbol.mostrar_arbol())
arbol.inorden()
print(" ")
arbol.postorden()
print(" ")
arbol.preorden()

