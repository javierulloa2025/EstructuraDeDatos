"""En Python, la palabra clave yield se utiliza para definir una función generadora. 
A diferencia de return, que termina la función y devuelve un valor, 
yield suspende la ejecución de la función y devuelve un valor, 
pero conserva el estado de la función para que pueda reanudarse más tarde."""

def cuadrado():
    for i in range(1, 4):
        yield i*i

s = cuadrado()
print(list(s))   #Salida [1, 4, 9]