import random

class Dado():
    #atributos
    cantidad_lados = None
    lado_actual = None

    #Métodos
    def __init__(self, lados):
        if lados < 2:
            raise ("El dado debe tener al menos 2 lados")
        self.cantidad_lados = lados
        self.lado_actual = 1 #Valor inicial (antes de lanzar el dado)
    
    def lanzar_dado(self):   #Simula el lanzamiento
        self.lado_actual = random.randint(1, self.cantidad_lados)
        return self.lado_actual
    
    def obtener_lado_actual(self): #devolver la cara actual
        if self.lado_actual is None:
            raise ValueError("El dado no ha sido lanzado aun")
        return self.lado_actual
    
    def simular_lanzamientos(self, n):
        contador = {}

        # inicializar contador
        for i in range(1, self.cantidad_lados + 1):
            contador[i] = 0

        # realizar lanzamientos
        for i in range(n):
            resultado = self.lanzar_dado()
            contador[resultado] += 1

        return contador

lados = 6
dadoseis = Dado(lados)
resultado = dadoseis.simular_lanzamientos(12000000)
print(resultado)