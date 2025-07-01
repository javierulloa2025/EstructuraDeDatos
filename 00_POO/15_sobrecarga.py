def multiplicacion(a, b, c=None, d=None):
    if c != None:
        if d != None:
            print(a * b * c * d)
        else:
            print(a * b * c)
    else:
        print(a * b)

multiplicacion(10, 3, 4, 5)