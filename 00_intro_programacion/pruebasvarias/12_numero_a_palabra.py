num = int(input("Introduce un número: "))
def numero_a_palabra(num):
    unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco",
                "seis", "siete", "ocho", "nueve", "diez", "once",
                "doce", "trece", "catorce", "quince", "dieciseis",
                "diecisiete", "dieciocho", "diecinueve"
                ]
    decenas = ["", "", "veinte", "treinta", "cuarenta", "cincuenta",
               "sesenta", "setenta", "ochenta", "noventa"
               ]
    
    if num < 20:
        return unidades[num]
    elif num < 100:
        return decenas [num // 10] + ('' if num % 10 == 0 else " " + unidades[num % 10])
    elif num < 1000:
        pass

print(numero_a_palabra(num))
    