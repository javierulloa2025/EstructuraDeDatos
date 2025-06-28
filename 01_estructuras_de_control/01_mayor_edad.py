try:
    edad = int(input("Dime tu edad: "))
    if edad < 18:
        print("Eres menor de edad")
    else:
        print("Eres mayor de edad")
except ValueError:
    print("debes introducir un número")


    