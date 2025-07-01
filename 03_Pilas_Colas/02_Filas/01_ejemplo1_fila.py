from claseFila import Fila

#Crear fila de clientes
 
fila_tienda = Fila()

#llegan clientes
fila_tienda.encolar ("Cliente 1")
fila_tienda.encolar ("Cliente 2")
fila_tienda.encolar ("Cliente 3")

# Atender clientes
print(f"Atendiendo a {fila_tienda.quitar()}") #Atendiendo cliente 1, 2, o 3
print(f"Próximo en la fila: {fila_tienda.frente()}")

