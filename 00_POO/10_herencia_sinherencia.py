class Ciudadano:
    def __init__(self,nombre, profesion):
        self.nombre = nombre
        self.profesion = profesion
    
    def saludar(self):
        print(f"Hola soy {self.nombre}. Mi profesión es {self.profesion}")

class Medico:
    def __init__(self,nombre):
        self.nombre = nombre
        self.profesion = "medico"
    def saludar(self):
        print(f"Hola soy {self.nombre}. Mi profesión es {self.profesion}")


a = Ciudadano("Juan", "Ingeniero")
b = Medico("Jenifer")

a.saludar()
b.saludar()