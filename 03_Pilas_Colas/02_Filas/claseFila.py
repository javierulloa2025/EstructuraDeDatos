class Fila:
    #Constructor
    def __init__(self):
        self.elementos = []

    #encolar un elemento
    def encolar(self, dato):
        self.elementos.append(dato)

    #Está vacía?
    def esta_vacia(self):
        return len(self.elementos)==0
    
    #Sacar un elemento
    def quitar(self):
        if self.esta_vacia():
            print("la lista está vacía, retorna None")
            return None
        return self.elementos.pop(0)
    
    #limpiar fila
    def limpiar(self):
        del self.elementos[:]  #otra opción es self.elementos.clear()

    #frente de la fila
    def frente(self):
        if self.esta_vacia():
            print("La lista está vacía, retorna None")
            return None
        return self.elementos[0]
    
    #tamaño de la fila
    def tamanio(self):
        return len(self.elementos)
    
    #Mostrar elementos de la fila
    def mostrar_elementos(self):
        print("Los elementos de la fila son:")
        print(self.elementos)
