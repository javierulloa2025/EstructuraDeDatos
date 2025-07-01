#Ejemplo 2: procesando tareas de un servidor con filas

from claseFila import Fila

#Crear fila de tareas
fila_tareas = Fila()

#Agregar tareas
fila_tareas.encolar("Respaldo de la BD")
fila_tareas.encolar("Actualizar API")
fila_tareas.encolar("Enviar emails")

#Procesar tareas
while True:
    tarea = fila_tareas.quitar()
    if tarea is None:
        print("No hay más tareas!")
        break
    print (f"Procesando tarea {tarea}")



