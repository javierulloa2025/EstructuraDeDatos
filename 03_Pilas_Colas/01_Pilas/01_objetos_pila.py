from clasePila import Pila

#ejemplos

p = Pila()

vacia = p.esta_vacia()
print(vacia)

p.insertar("H")
p.insertar("O")
p.insertar("L")
p.insertar("A")
p.mostrar_elementos()

while(not p.esta_vacia()):
    print(p.quitar_elemento())


#Otro ejemplo

platos = Pila()

platos.insertar(1)
platos.insertar(2)
platos.insertar(3)
platos.insertar(4)

platos.mostrar_elementos()
platos.quitar_elemento()
platos.mostrar_elementos()
platos.insertar(5)
platos.mostrar_elementos()
platos.quitar_elemento()
platos.mostrar_elementos()
