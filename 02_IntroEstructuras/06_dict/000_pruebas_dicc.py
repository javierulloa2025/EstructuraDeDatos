diccionario = {
 "nombre" : "Francisco",
 "edad" : 45,
 "ciudad" : "Puerto Vallarta" 
}
diccionario["Profesion"] = "maestro"

for clave, valor in diccionario.items():
    print(f"Clave: {clave} y valor: {valor}")
