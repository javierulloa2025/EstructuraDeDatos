import random

class Dado():
    
    #Atributos
    cantidad_lados = None
    lado_actual = None

    #Métodos
    def __init__(self, lados):
        if lados < 2:
            raise ValueError ("El dado debe tener al menos 2 lados")
        self.cantidad_lados = lados
        self.lado_actual = 1  #Valor inicial antes del primer lanzamiento
        
    def lanzar_dado(self):
        """Simula el lanzamiento del dado y devuelve el resultado"""
        self.lado_actual = random.randint(1, self.cantidad_lados)
        return self.lado_actual

    def obtener_lado_actual(self):
        """Devuelve el valor actual del dado (ultimo lanzamiento)"""
        if self.lado_actual is None:
            raise ValueError("El dado no ha sido lanzado aún")
        return self.lado_actual
    
    def __str__ (self):
        return (f"El dado de {self.cantidad_lados} lados, dio como resultado: {self.lado_actual}")


# Ejemplo de uso:
lados=20
dadoseis = Dado(lados)
dadoseis.lanzar_dado()
resultado = dadoseis.obtener_lado_actual()
print(f"El resultado de lanzar un dado de {lados} lados fue: {resultado}")
