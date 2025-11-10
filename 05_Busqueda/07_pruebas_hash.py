# Hash diferentes tipos de datos
number = 42
text = "Python Programming"
decimal = 3.14159

# Calcular los valores hash
number_hash = hash(number)
text_hash = hash(text)
decimal_hash = hash(decimal)

# Mostrar el resultado
print(f"Hash de {number}: {number_hash}")
print(f"Hash de '{text}': {text_hash}")
print(f"Hash de {decimal}: {decimal_hash}")
