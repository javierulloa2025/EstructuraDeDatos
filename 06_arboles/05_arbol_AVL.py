class ArbolAVL:
    def __init__(self, valor=None):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1 if valor is not None else 0

    # ============================
    # FUNCIONES AUXILIARES
    # ============================

    def obtener_altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def obtener_balance(self):
        """Devuelve el factor de equilibrio del nodo actual"""
        return self.obtener_altura(self.izquierdo) - self.obtener_altura(self.derecho)

    def actualizar_altura(self):
        """Actualiza la altura del nodo actual"""
        self.altura = 1 + max(self.obtener_altura(self.izquierdo),self.obtener_altura(self.derecho))

    def encontrar_min(self):
        """Encuentra el nodo con el valor mínimo en el subárbol actual"""
        actual = self
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual

    # ============================
    # ROTACIONES
    # ============================

    def rotacion_derecha(self):
        """Rotación simple a la derecha"""
        nueva_raiz = self.izquierdo
        subarbol_derecho = nueva_raiz.derecho

        # Rotar
        nueva_raiz.derecho = self
        self.izquierdo = subarbol_derecho

        # Actualizar alturas
        self.actualizar_altura()
        nueva_raiz.actualizar_altura()

        return nueva_raiz

    def rotacion_izquierda(self):
        """Rotación simple a la izquierda"""
        nueva_raiz = self.derecho
        subarbol_izquierdo = nueva_raiz.izquierdo

        # Rotar
        nueva_raiz.izquierdo = self
        self.derecho = subarbol_izquierdo

        # Actualizar alturas
        self.actualizar_altura()
        nueva_raiz.actualizar_altura()

        return nueva_raiz

    # ============================
    # INSERCIÓN BALANCEADA
    # ============================

    def insertar(self, valor):
        if self.valor is None:
            self.valor = valor
            self.altura = 1
            return self

        # Inserción normal (BST)
        if valor < self.valor:
            if self.izquierdo is None:
                self.izquierdo = ArbolAVL(valor)
            else:
                self.izquierdo = self.izquierdo.insertar(valor)
        else:
            if self.derecho is None:
                self.derecho = ArbolAVL(valor)
            else:
                self.derecho = self.derecho.insertar(valor)

        # Actualizar altura
        self.actualizar_altura()

        # Verificar balance
        balance = self.obtener_balance()

        # Caso Izquierda - Izquierda
        if balance > 1 and valor < self.izquierdo.valor:
            return self.rotacion_derecha()

        # Caso Derecha - Derecha
        if balance < -1 and valor > self.derecho.valor:
            return self.rotacion_izquierda()

        # Caso Izquierda - Derecha
        if balance > 1 and valor > self.izquierdo.valor:
            self.izquierdo = self.izquierdo.rotacion_izquierda()
            return self.rotacion_derecha()

        # Caso Derecha - Izquierda
        if balance < -1 and valor < self.derecho.valor:
            self.derecho = self.derecho.rotacion_derecha()
            return self.rotacion_izquierda()

        return self

    # ============================
    # ELIMINACIÓN BALANCEADA
    # ============================

    def eliminar_nodo(self, valor):
        if self.valor is None:
            return self

        # Búsqueda estándar BST
        if valor < self.valor:
            if self.izquierdo:
                self.izquierdo = self.izquierdo.eliminar_nodo(valor)
        elif valor > self.valor:
            if self.derecho:
                self.derecho = self.derecho.eliminar_nodo(valor)
        else:
            # Caso 1: sin hijos
            if not self.izquierdo and not self.derecho:
                return None
            # Caso 2: un hijo
            elif not self.izquierdo:
                return self.derecho
            elif not self.derecho:
                return self.izquierdo
            # Caso 3: dos hijos → reemplazar con el mínimo del subárbol derecho
            sucesor = self.derecho.encontrar_min()
            self.valor = sucesor.valor
            self.derecho = self.derecho.eliminar_nodo(sucesor.valor)

        # Actualizar altura
        self.actualizar_altura()

        # Rebalancear
        balance = self.obtener_balance()

        # Caso Izquierda - Izquierda
        if balance > 1 and self.izquierdo.obtener_balance() >= 0:
            return self.rotacion_derecha()
        # Caso Izquierda - Derecha
        if balance > 1 and self.izquierdo.obtener_balance() < 0:
            self.izquierdo = self.izquierdo.rotacion_izquierda()
            return self.rotacion_derecha()
        # Caso Derecha - Derecha
        if balance < -1 and self.derecho.obtener_balance() <= 0:
            return self.rotacion_izquierda()
        # Caso Derecha - Izquierda
        if balance < -1 and self.derecho.obtener_balance() > 0:
            self.derecho = self.derecho.rotacion_derecha()
            return self.rotacion_izquierda()

        return self

    # ============================
    # RECORRIDOS
    # ============================

    def preorden(self):
        """Recorrido en preorden (raíz, izquierda, derecha)"""
        if self.valor is not None:
            print(self.valor, end=" ")
            if self.izquierdo:
                self.izquierdo.preorden()
            if self.derecho:
                self.derecho.preorden()
    
    # Mostrar
    def mostrar_arbol(self, nivel=0, prefijo="Raíz: "):
        resultado = "    " * nivel + prefijo + str(self.valor) + "\n"
        if self.izquierdo:
            resultado += self.izquierdo.mostrar_arbol(nivel + 1, "Izq: ")
        if self.derecho:
            resultado += self.derecho.mostrar_arbol(nivel + 1, "Der: ")
        return resultado      

arbol = ArbolAVL()
for v in [30, 20, 40, 10, 25, 35, 50]:
    arbol = arbol.insertar(v)

print("Preorden del árbol AVL balanceado:")
arbol.preorden()

#arbol = arbol.eliminar_nodo(20)
#print("\nPreorden tras eliminar 20:")
arbol.preorden()
print(arbol.mostrar_arbol())