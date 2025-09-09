class DatoPolinomio(object):
    """Clase dato polinomio"""
    def __init__(self, valor, termino):
        """Crea un dato polinomio con valor y termino"""
        self.valor = valor
        self.termino = termino

class Polinomio(object):
    """Clase polinomio"""

    def __init__(self):
        """Crea un polinomio de grado cero"""
        self.termino_mayor = None
        self.grado = -1

class Nodo(object):
    """Clase nodo simple enlazado"""
    info, sig = None, None

aux = Nodo()

aux.info="Primer nodo"
palabra = input("Ingrese una palabra: ")
naux = aux
while (palabra != ""):
    nodo = Nodo()
    nodo.info= palabra
    naux.sig = nodo
    naux = nodo
    palabra = input("Ingrese una palabra: ")

while (aux is not None):
    print(aux.info)
    aux = aux.sig

