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
        if self.valor is None:
            return -1
        
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
        if self.valor is None:  #árbol vacío
            return None
        if self.izquierdo is None:
            return self
        else:
            return self.izquierdo.encontrar_min()

    def encontrar_max(self):
        if self.valor is None:
            return None
        if self.derecho is None:
            return self.valor
        else:
            return self.derecho.encontrar_max()

#Recorridos DFS
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

#Recorridos BFS
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

# Dibujar árbol en ASCII (función opcional, generada con IA)
    def dibujar_ascii(self):

        def _dibujar(nodo):
            if nodo is None or nodo.valor is None:
                return [], 0, 0

            # Subárboles
            lineas_izq, ancho_izq, centro_izq = _dibujar(nodo.izquierdo)
            lineas_der, ancho_der, centro_der = _dibujar(nodo.derecho)

            s = str(nodo.valor)
            ancho_s = len(s)

            # Caso: nodo sin hijos
            if ancho_izq == 0 and ancho_der == 0:
                return [s], ancho_s, ancho_s // 2

            # Normalizar alturas de subárboles
            alto_izq = len(lineas_izq)
            alto_der = len(lineas_der)
            alto = max(alto_izq, alto_der)

            while len(lineas_izq) < alto:
                lineas_izq.append(" " * ancho_izq)
            while len(lineas_der) < alto:
                lineas_der.append(" " * ancho_der)

            espacio_entre = 1
            ancho_total = ancho_izq + espacio_entre + ancho_s + espacio_entre + ancho_der
            centro = ancho_izq + espacio_entre + ancho_s // 2

            # Línea del nodo (centrada)
            linea_raiz = (
                (" " * ancho_izq) +
                (" " * espacio_entre) +
                s +
                (" " * espacio_entre) +
                (" " * ancho_der)
            )

            # Línea de conexiones
            linea_conex = [" "] * ancho_total
            if ancho_izq > 0:
                pos_slash = centro_izq
                linea_conex[pos_slash] = "/"
            if ancho_der > 0:
                pos_back = ancho_izq + espacio_entre + ancho_s + centro_der
                linea_conex[pos_back] = "\\"

            linea_conex_str = "".join(linea_conex)

            # Combinar subárboles
            combinado = []
            espacio_central = espacio_entre + ancho_s + espacio_entre
            for i in range(alto):
                combinado.append(
                    lineas_izq[i] +
                    (" " * espacio_central) +
                    lineas_der[i]
                )

            # Salida final
            salida = [linea_raiz, linea_conex_str] + combinado
            return salida, ancho_total, centro

        lineas, _, _ = _dibujar(self)
        return "\n".join(lineas) if lineas else "Árbol vacío"