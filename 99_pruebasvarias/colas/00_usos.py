from claseFila import Fila

fila_tienda = Fila()

#Formarlos
fila_tienda.enconlar("Cliente 1")
fila_tienda.enconlar("Cliente 2")
fila_tienda.enconlar("Cliente 3")
fila_tienda.enconlar("Cliente 4")
fila_tienda.enconlar("Cliente 5")

#Atenderlos
tamano = fila_tienda.tamano()
print(f"Por atender {tamano}")
for cliente in range(tamano):
    frente = fila_tienda.frente()
    print(f"Atendiendo a {frente}")
    fila_tienda.quitar()
    frente = fila_tienda.frente()
    if not fila_tienda.vacia():
        print(f"Próximo cliente {frente}")
    else:
        print("Fila vacía")
    print(f"Clientes restantes: {fila_tienda.tamano()}")
    print("--------------------------")
