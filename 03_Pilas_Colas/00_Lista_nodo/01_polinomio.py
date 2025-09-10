from claseNodo import Nodo

class datoPolinomio(object):
    """Clase dato polinomio"""
    
    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y término"""
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    """Clase polinomio"""

    def __init__(self):
        """Crea un polinomio de grado cero"""
        self.termino_mayor = None
        self.grado = -1
    
def agregar_termino(polinomio, termino, valor):
    """Agrega un termino y su valor al polinomio"""
    aux = Nodo()
    dato = datoPolinomio(valor, termino)
    aux.info = dato
    
    # Si el polinomio está vacío o el término es mayor al grado actual
    if polinomio.termino_mayor is None or termino > polinomio.grado:
        aux.sig = polinomio.termino_mayor
        polinomio.termino_mayor = aux
        polinomio.grado = termino
    else:
        actual = polinomio.termino_mayor
        # Si el nuevo término es menor que el término mayor
        if termino < actual.info.termino:
            # Buscar la posición correcta para insertar
            while actual.sig is not None and termino < actual.sig.info.termino:
                actual = actual.sig
            aux.sig = actual.sig
            actual.sig = aux
        # Si el término ya existe, actualizar el valor
        elif termino == actual.info.termino:
            actual.info.valor += valor
        else:
            # Insertar al principio
            aux.sig = polinomio.termino_mayor
            polinomio.termino_mayor = aux

def mostrar(polinomio):
    """muestra el polinomio"""
    aux = polinomio.termino_mayor
    pol = ""
    if aux is not None:
        while aux is not None:
            signo = " "
            if aux.info.valor >= 0 and pol != "":
                signo += "+"
            elif aux.info.valor < 0:
                signo += "-"
            
            valor_abs = abs(aux.info.valor)
            if valor_abs != 1 or aux.info.termino == 0:
                pol += signo + str(valor_abs)
            if aux.info.termino > 0:
                pol += "x"
                if aux.info.termino > 1:
                    pol += "^" + str(aux.info.termino)
            aux = aux.sig
    
    return pol.strip()

# Crear y probar el polinomio
p = Polinomio()
agregar_termino(p, 2, 3)  # 3x²
agregar_termino(p, 1, 2)  # + 2x
agregar_termino(p, 0, 1)  # + 1
agregar_termino(p, 3, -4) # - 4x³

print("Polinomio:", mostrar(p))  # Resultado: -4x^3 + 3x^2 + 2x + 1

