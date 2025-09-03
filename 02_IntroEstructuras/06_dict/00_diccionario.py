midiccionario = {
    "nombre": "Francisco Javier",
    "apellido": "Ulloa",
    "edad": 25,
    "ciudad": "Puerto Vallarta",

}

print(midiccionario["nombre"])
print(midiccionario["edad"])
midiccionario["profesion"] = "programador"
print(midiccionario)
midiccionario["edad"] = 26

print(midiccionario)

for key, value in midiccionario.items():
    print(f"La clave es: {key}, el valor es: {value}")