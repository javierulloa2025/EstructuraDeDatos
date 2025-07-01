class Ciudadano:
    def __init__(self,nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    
    def saludar(self):
        print(f"Hola soy {self.nombre}. Mi profesión es {self.profesion}")

class Medico(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, profesion = "Médico")
    def recetar_paracetamol(self):
        print(f"Soy {self.nombre}, aquí tiene su paracetamol")

class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "policia")
    def pedir_refuerzos(self):
        print(f"A todas las unidades, soy {self.nombre} y solicito refuerzos")

individuo1 = Policia("Pedro")
individuo2 = Medico("Dr. House")

individuo1.pedir_refuerzos()
individuo2.recetar_paracetamol()