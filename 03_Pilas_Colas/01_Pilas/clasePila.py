class Pila:
#Constructor
  def __init__(self):
    self.elementos = []

#Insertar un elemento
  def insertar(self,dato):
    self.elementos.append(dato)

# ¿Está vacía?
  def esta_vacia(self):
    return len(self.elementos) == 0

#Sacar un elemento
  def quitar_elemento(self):
    if self.esta_vacia():
        print ("La lista está vacía, retorna None")
        return None
    return self.elementos.pop()

#Limpiar la pila
  def limpiar_pila(self):
    self.elementos.clear()
    
#Cima de la pila
  def cima(self):
    if self.esta_vacia():
        print ("La lista está vacía, retorna None")
        return None
    return self.elementos[-1]

#Tamaño de la pila
  def tamanio(self):
    return len(self.elementos)

#Mostrar elementos de la pila
  def mostrar_elementos(self):
    return f"Los elementos de la pila son: {self.elementos[::-1]}"
    

#Método especial string para imprimir directamente la lista
  def __str__(self):
    return f"Pila: {self.elementos}"
  
#Método especial len para obtener el tamaño
  def __len__(self):
    return len(self.elementos)