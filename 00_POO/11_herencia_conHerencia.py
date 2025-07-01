class Ciudadano:
    def __init__(self,nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    
    def saludar(self):
        print(f"Hola soy {self.nombre}. Mi profesión es {self.profesion}")

class Medico(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, profesion = "Médico")
    

a = Medico("Javier")

a.saludar()
