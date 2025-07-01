def factory(n):
    return lambda x: x ** n

cuadrado = factory(2)
cubo = factory(3)

print(cuadrado(3), cubo (2))