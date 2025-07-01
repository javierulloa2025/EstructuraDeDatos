#Sucesión de Fibonacci con recursividad

def fib(n):
    if n == 0 or n == 1:  #Caso base
        return n
    else:
        return fib(n-1) + fib(n-2)
    
for numero in range(0, 12):
    print(f"{fib(numero)}", end=" ")