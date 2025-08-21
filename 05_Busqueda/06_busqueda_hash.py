def funcion_hash(clave, tamano_tabla):
    return hash(clave) % tamano_tabla

class TablaHash:
    def __init__(self, tamano = 10):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]

    def insertar(self, clave, valor):
        indice = funcion_hash(clave, self.tamano)
        self.tabla[indice].append((clave, valor))

    def buscar(self, clave):
        indice = funcion_hash(clave, self.tamano)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None
    
    def eliminar(self,clave):
        indice = funcion_hash(clave, self.tamano)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                del self.tabla[indice][i]
                return True
        return False

    def __str__(self):
        return f"{self.tabla}"
#Uso
tejemplo = TablaHash()
tejemplo.insertar("nombre", "Javier")
tejemplo.insertar("edad", 45)
print(tejemplo.buscar("nombre")) #salida Javier
print(tejemplo.buscar("edad")) #salida 45
print(tejemplo.buscar("telefono")) #salida None
print(tejemplo) #salida la tabla completa (usa __str__)
