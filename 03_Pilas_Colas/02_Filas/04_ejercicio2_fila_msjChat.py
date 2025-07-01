from claseFila import Fila

#Instanciamos
fila_mensajes = Fila()

#listado de mensajes
mensajes = ["Hola", "Buenos dias", "adios", "URGENTE", "besos"]

for msj in mensajes:
    fila_mensajes.encolar(msj)

while not fila_mensajes.esta_vacia():
    if "URGENTE" in fila_mensajes.elementos:  #busca URGENTE
        indice_urgente = fila_mensajes.elementos.index("URGENTE") #obtiene el indice de "URGENTE"
        urgente = fila_mensajes.elementos.pop(indice_urgente) #saca el elemento URGENTE en la posicion indice_urgente
        print(f"Procesando {urgente} (mensaje urgente)")
    else:
        print(f"Procesando: {fila_mensajes.quitar()}")
    print(f"Fila actual: {fila_mensajes.elementos}")
    print("----")
