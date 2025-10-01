class Fila:
    #Constructor
    def __init__(self):
        self.elementos = []

    #encolar un elemento
    def enconlar(self, dato):
        self.elementos.append(dato)

    #¿está vacía?
    def vacia(self):
        return len(self.elementos) == 0

    #quitar un elemento
    def quitar(self):
        if self.vacia():
            print("Fila vacía")
            return None
        return self.elementos.pop(0)

    #limpiar la fila
    def limpiar(self):
        self.elementos.clear()

    # frente de la fila
    def frente(self):
        if self.vacia():
            print("Fila vacía")
            return None
        return self.elementos[0]

    #tamaño de la fila
    def tamano(self):
        return len(self.elementos)

    #mostrar elementos
    def mostrar_elementos(self):
        print("Los  elementos de la fila son: ")
        print(self.elementos)