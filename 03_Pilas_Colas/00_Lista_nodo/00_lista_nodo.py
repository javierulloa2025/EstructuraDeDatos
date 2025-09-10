from claseNodo import Nodo

#Crear el primer nodo
cabeza = Nodo()
cabeza.info = "Primer nodo"


#Crear lista enlazada
palabra = input("Ingrese una palabra, o Enter vacío para terminar: ")
actual = cabeza #actual apunta al último nodo
while palabra != "":
    nuevo_nodo = Nodo()  #Crea un nuevo nodo
    nuevo_nodo.info = palabra  #Asigna la palabra
    actual.sig = nuevo_nodo  #Enlaza con el anterior
    actual = nuevo_nodo      #Actualiza el último nodo
    palabra = input("Ingrese otra palabra: ")

#Recorrer e imprimir
print("Lista completa: ")
actual = cabeza #Volvemos al inicio para recorrer
while actual is not None:
    print(actual.info)
    actual = actual.sig


    