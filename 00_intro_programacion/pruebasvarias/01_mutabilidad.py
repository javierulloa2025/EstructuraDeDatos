"""a = 5
b = a #b apunta a la zona de memoria de a
print(id(a))
print(id(b))  #ambas variables apuntan a la misma zona de memoria
"""
#Datos mutables
#Ejemplo con lista
a = [ 4, 3, 2]
b = a  #no se hace una copia, están en la misma memoria

print(id(a))
print(id(b))

a.append(1)  #Agregamos un elemento nuevo a la lista a

print(b) # también se afectó b!!!!!

