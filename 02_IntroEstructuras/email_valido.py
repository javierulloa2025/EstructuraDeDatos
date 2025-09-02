import re

def es_email_valido(email):
    """
    Comprueba si un correo electrónico tiene un formato válido usando una expresión regular.
    """
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(patron, email):
        return True
    else:
        return False

correo_ejemplo = "javier_ulloa@cualtos.udg.mx"

print(es_email_valido(correo_ejemplo))