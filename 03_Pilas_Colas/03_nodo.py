class Nodo(object):
    """Clase Nodo"""
    info, sig, iden = None, None, None

#creando el primer nodo
cabeza = Nodo()
cabeza.info = "1er nodo"
cabeza.iden = 1

#crear la lista enlazada
palabra = input("Ingresa la palabra o enter para terminar: ")
actual = cabeza  #apunta al último nodo
while palabra != "":
    nuevo_nodo = Nodo()   #Crea un nuevo nodo
    nuevo_nodo.info = palabra  #asigna la palabra ingresada
    actual.sig = nuevo_nodo #enlaza los nodos
    actual = nuevo_nodo #Actualizar el último nodo 
    palabra = input("Ingresa otra palabra, enter para terminar: ")

#recorrer e imprimir
print("Lista completa: ")
actual = cabeza #Volvemos al inicio
while actual is not None:
    print(f"Identificador: {actual.ide} valor {actual.info}")
    actual = actual.sig 

 