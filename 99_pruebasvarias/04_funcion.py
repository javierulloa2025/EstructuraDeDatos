#Error 1: un problema de ámbito (scope) de variable
#Error 2: la función no retorna nada
#Error 3: aunque retornara "nombre" habría que asignarlo a una variable global, que igual puede llamarse nombre

def establecer_nombre():
    nombre = "Python"
    
establecer_nombre()
print(nombre)

""" Código corregido:
def establecer_nombre():
    nombre = "Python"
    return nombre

nombre = establecer_nombre()
print(nombre)
"""