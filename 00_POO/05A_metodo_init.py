class Usuario:
    
    #Metodo constructor con atributos de instancia
    def __init__(self, nombre, apellidos, 
                 edad, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono
        self.direccion = "sin dirección"

usuario1 = Usuario("Mario","Perez",34,33102)

print(usuario1.direccion)



