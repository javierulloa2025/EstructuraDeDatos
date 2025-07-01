#Con la clase fila
#Crear una fila llamada fila_supermercado
#Encolar al menos 5 clientes (nombres o números)
#Simula la atención de los clientes (quitando de uno en uno)
#Después de atender a cada cliente muestra:
#   El cliente atendido
#   El próximo cliente en la fila
#   La cantidad restante de clientes

from claseFila import Fila

fila_supermercado = Fila()

#Encolar
fila_supermercado.encolar("Cliente 1")
fila_supermercado.encolar("Cliente 2")
fila_supermercado.encolar("Cliente 3")
fila_supermercado.encolar("Cliente 4")
fila_supermercado.encolar("Cliente 5")

#Atender
tamanio = fila_supermercado.tamanio()
print(f"Por atender {tamanio} clientes")
for cliente in range (tamanio):
    frente = fila_supermercado.frente()
    print(f"Atendiendo a {frente}")
    fila_supermercado.quitar()
    frente = fila_supermercado.frente()
    if not fila_supermercado.esta_vacia():
        print(f"Próximo cliente {frente}")
    else:
        print("Fila vacia")
    print(f"Clientes restantes: {fila_supermercado.tamanio()}")
    print("-----")
