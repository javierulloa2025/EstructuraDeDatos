class Perro():
    #atributo de clase
    especie = "Canino"

    def __init__(self,nombre):
        self.nombre = nombre     #atributo de instancia


#Acceso a atribudo de instancia
mi_perro = Perro("Kira")
print(mi_perro.nombre)  #Salida Kira
mi_perro.color = "Blanco y negro" #Atributo de objeto creado al vuelo

#Acceso a atributo de clase
print(Perro.especie)
print(mi_perro.especie)
print(mi_perro.color)

print(Perro.color)  #Error la clase Perro no tiene el atributo color