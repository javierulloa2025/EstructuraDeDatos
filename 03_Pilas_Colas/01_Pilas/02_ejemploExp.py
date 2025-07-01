def esCorrecta_v1(exp_cadena):
    """Funcion que determina si una expresión es correcta Método 1 (sin uso de Pila)"""
    expresion = list(exp_cadena)
    seguir = True #Bandera que indica si debemos seguir
    while seguir:
        seguir = False
        for i in range(len(expresion)-1):
            a = expresion[i]
            b = expresion[i+1]
            if (a == "{" and b == "}") or (a == "(" and b == ")") or (a == "[" and b == "]"):
                del expresion[i] #mueve los demás elementos a la izquierda
                del expresion[i] #borra el siguiente elemento, no es necesario i+1 porque ya borró el anterior
                seguir = True
                break
    
    #Si la expresión es correcta, la lista debe estar vacía
    return len(expresion) == 0


#Casos de prueba
exp1 = "{{[[]()[]{}]}}"  #debe ser correcto
exp2 = "{{[[]()[]{}}]}"   #debe ser falso
exp3 = "{}[(({}){})]"  #debe ser correcto
exp4 = "{}[((}{}){})]"  #debe ser falso (elemento pos 5)
exp5 = "{}[{(({}){})]"  #debe ser falso (elemento pos 3)
exp6 = "({}[(({}){})]" #debe ser falso ("sobra el parentesis de inicio")
exp7 = "{}[(({}){})])" #debe ser falso (ver  el último elemento) 
exp8 = "({}{}[]())" #debe ser correcta


print(esCorrecta_v1(exp1))
print(esCorrecta_v1(exp2))
print(esCorrecta_v1(exp3))
print(esCorrecta_v1(exp4))
print(esCorrecta_v1(exp5))
print(esCorrecta_v1(exp6))
print(esCorrecta_v1(exp7))
print(esCorrecta_v1(exp8))
