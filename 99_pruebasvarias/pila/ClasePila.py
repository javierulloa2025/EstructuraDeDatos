class Pila:
#Constructor
    def __init__(self):
        self.elementos = []

#Insertar un elemento (push)
    def insertar(self, dato):
        self.elementos.append(dato)

#¿Está vacía?
    def vacia(self):
        return len(self.elementos) == 0
    
#Sacar un elemento (pop)
    def quitar_elemento(self):
        if self.vacia():
            print("lista vacía")
            return None
        return self.elementos.pop()

#Limpiar la pila
    def limpiar(self):
        self.elementos.clear()

#Cima de la pila 
    def cima(self):
        if self.vacia():
            print("pila vacía")
            return None
        return self.elementos[-1]    

#Tamaño de la pila
    def tamano(self):
        return len(self.elementos)
    
#Mostrar elementos de la pila
    def mostrar_elementos(self):
        return(f"Los elementos de la pila son: {self.elementos[::-1]}")
    
