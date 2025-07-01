class Usuario:
    #Atributos de clase
    hora_de_inicio = None

    #Métodos
    #Metodo constructor con atributos de instancia
    def __init__(self, nombre, apellidos, 
                 edad, direccion,telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.direccion = direccion
        self.telefono = telefono

    def iniciar_sesion(self):
        print("El usuario ha iniciado sesión")
    def cerrar_sesion(self):
        print ("El usuario ha cerrado sesión")
    def cambiar_nombre_perfil(self):
        print("Se cambió el nombre")

usuario1 = Usuario("Mario","Perez",34,"Av Parque",33102)


print(usuario1.nombre)
print(usuario1.hora_de_inicio)


