#Tres formas distintas de invertir una lista

# 1) Con slicing
shopping = ["Agua" , "Huevos", "Aceite", "Sal", "Limón"]
print(shopping[::-1])

# 2) Mediante función reversed() (no modifica la lista original)
print(list(reversed(shopping)))

# 3) Función reverse() (modifica la lista original)
print(list(reversed(shopping)))
