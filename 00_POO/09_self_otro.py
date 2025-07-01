class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad      # Otro atributo
    
    def presentarse(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear una instancia
p = Persona("Francisco", 45)
p.presentarse()  # Imprime: Hola, soy Francisco y tengo 45 años.