try:
    edad = int(input("Edad: "))
    print(f"Tienes {edad} años")
except ValueError:
    print("Debes ingresar un número!")