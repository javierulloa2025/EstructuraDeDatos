#Combina estos diccionarios sumando valores de claves comunes
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 40}
dict3 = {"a": 20, "b": 15, "c": 30, "d":5}

#Copiamos dict1
resultado = dict1.copy()

#Con "get"
for clave, valor in dict2.items( ): 
    resultado[clave] = resultado.get(clave, 0) + valor

"""
#Con for y condicionales
for clave, valor in dict2.items():
    if clave in resultado:
        resultado[clave] += valor
    else:
        resultado[clave] = valor    
"""

#Imprimimos resultado
print(resultado)
