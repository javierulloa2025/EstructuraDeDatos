num = int(input("Escribe un número entero: "))

for i in range(1, num-1):
    num += num * i

print(num)

"""
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)
"""