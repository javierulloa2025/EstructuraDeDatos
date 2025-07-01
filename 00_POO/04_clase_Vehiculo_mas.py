class Vehiculo():
    #Atributos
    color = None
    longitud_metros = None
    ruedas = 4

    #Métodos
    def arrancar(self):
        print("El motor ha encendido")
    
    def apagar(self):
        print("El auto se ha apagado")

mustang = Vehiculo()

mustang.arrancar()

ruedas_mustang = mustang.ruedas

#dos formas diferentes de acceder a los atributos
print(f"El vehiculo mustang tiene {mustang.ruedas} ruedas")
print(f"El vehiculo mustang tiene {ruedas_mustang} ruedas")

