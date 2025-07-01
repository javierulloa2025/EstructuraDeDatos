#Crear atributos adicionales a un objeto

class Vehiculo():
    #Atributos
    color = None
    longitud_metros = None
    ruedas = 4

carro1 = Vehiculo()
carro2 = Vehiculo()

carro1.velocidad_max = 200

print(carro1.velocidad_max)  #imprime 200
print(carro2.velocidad_max)  #arroja un error: "el objeto carro2 no tiene el atributo vel_max"



