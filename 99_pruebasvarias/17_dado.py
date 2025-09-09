import random

class Dado():
    #Atributros
    cantidad_de_lados = None
    lado_actual = None

    #Métodos
    def __init__(self, lados):
        if lados <= 2:
            raise ValueError ("La cantidad de lados debe ser al menos 2")
        self.cantidad_de_lados = lados
        self.lado_actual = 1

    def lanzar_dado(self):
        """Simula el lanzamiento aleatorio del dado"""
        self.lado_actual = random.randint(1, self.cantidad_de_lados)
        return self.lado_actual

    def obtener_lado(self):
        """Devuelve el valor actual del lado (último lanzamiento)"""
        if self.lado_actual is None:
            raise ValueError ("El dado no ha sido lanzado")
        return self.lado_actual
    
    def __str__(self):
        return(f"El dado de {self.cantidad_de_lados} lados, \
                 dio como resultado {self.lado_actual}")

dado1 = Dado(6)
dado2 = Dado(6)

dado1.lanzar_dado()
dado2.lanzar_dado()

print(f"El dado 1: {dado1.obtener_lado()} y el dado 2: {dado2.obtener_lado()}")

