from clasePila import Pila

def esCorrecta_v2(exp_cadena):
    """Funcion que determina si una expresión es correcta
    método 2, usando Pilas
    """
    p = Pila()
    for sim in exp_cadena:
        if sim == "{" or sim == "[" or sim == "(":
            p.insertar(sim)
        if sim == "}" or sim == "]" or sim == ")":
            if p.esta_vacia():
                return False
            quitar = p.quitar_elemento()
            if (quitar == "{" and sim != "}") or (quitar == "[" and sim != "]") or (quitar == "(" and sim != ")"):
                return False

    return p.esta_vacia()     

#Casos de prueba
exp1 = "{{[[]()[]{}]}}"  #debe ser correcto
exp2 = "{{[[]()[]{}}]}"   #debe ser falso
exp3 = "{}[(({}){})]"  #debe ser correcto
exp4 = "{}[((}{}){})]"  #debe ser falso (elemento pos 5)
exp5 = "{}[{(({}){})]"  #debe ser falso (elemento pos 3)
exp6 = "({}[(({}){})]" #debe ser falso ("sobra el parentesis de inicio")
exp7 = "{}[(({}){})])" #debe ser falso (ver  el último elemento) 
exp8 = "({}{}[]())" #debe ser correcta

print(esCorrecta_v2(exp1))
print(esCorrecta_v2(exp2))
print(esCorrecta_v2(exp3))
print(esCorrecta_v2(exp4))
print(esCorrecta_v2(exp5))
print(esCorrecta_v2(exp6))
print(esCorrecta_v2(exp7))
print(esCorrecta_v2(exp8))
