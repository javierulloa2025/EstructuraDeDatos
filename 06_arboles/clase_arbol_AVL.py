class ArbolAVL:
    def __init__(self, valor=None):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1 if valor is not None else 0

    # FUNCIONES AUXILIARES

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
    
    def buscar_nodo(self, valor):
        """Devuelve el nodo con el valor indicado, si existe"""
        if self.valor is None:
            return None
        if valor == self.valor:
            return self
        elif valor < self.valor and self.izquierdo:
            return self.izquierdo.buscar_nodo(valor)
        elif valor > self.valor and self.derecho:
            return self.derecho.buscar_nodo(valor)
        return None


    # ROTACIONES

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

    # INSERCIÓN BALANCEADA

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

    # ELIMINACIÓN BALANCEADA

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

    # RECORRIDOS
    
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

    def obtener_info_nodo(self, valor):
        """Muestra la altura y el factor de equilibrio del nodo que contiene el valor indicado"""
        nodo = self.buscar_nodo(valor)
        if nodo is None:
            print(f"El valor {valor} no se encuentra en el árbol.")
            return
        altura_izq = self.obtener_altura(nodo.izquierdo)
        altura_der = self.obtener_altura(nodo.derecho)
        fe = altura_izq - altura_der
        print(f"Nodo {valor}: altura = {nodo.altura}, FE = {fe}")

    # Dibujar árbol en ASCII (opcional, generada IA)
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




