class Contador:
    """TDA contador, representa un contador basico
    con incremento, decremento y reset"""

    def __init__(self, valor_inicial = 0):
        self.__valor = valor_inicial

    def incrementar(self, cantidad = 1):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__valor += cantidad

    def decrementar(self, cantidad = 1):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__valor -= cantidad

    def reset(self):
        "Reinicia el contador a cero"
        self.__valor = 0

    def obtener_valor(self):
        return self.__valor
    
    def __str__(self):
        return f"Valor actual: {self.__valor}"
    
mi_contador = Contador()
print(mi_contador)
mi_contador.incrementar(10)
print(mi_contador)
mi_contador.reset()
mi_contador.incrementar(-4)
