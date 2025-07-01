#insert añade en cualquie posición de una lista
colores = ["azul","verde","rojo"]
colores.insert(1,"amarillo") #Inserta "amarillo" en la posición 1

print(colores) #Salida ['azul', 'amarillo', 'verde', 'rojo'] 


#Igual que en slicing, en insert no obtendremos un error si especificamos indices fuera de los limites

shopping = ["Agua", "Huevos", "Aceite"]
shopping.insert(100, "Mermelada") #Inserta en la posición inexistente "100"
shopping.insert(-100,"Arroz") #inserta en la posición inexistente "-100"
print(shopping)


