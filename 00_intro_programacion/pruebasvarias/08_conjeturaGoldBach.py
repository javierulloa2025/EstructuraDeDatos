def es_primo(numero):
    """Verifica si un número es primo."""
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def formas_de_sumar_primos(n):
    """
    Calcula las formas de expresar un número par como suma de dos primos.

    Args:   
       n: El número par a descomponer.

    Returns:
       El número de formas diferentes de expresar n como suma de dos primos.
    """
    if n <= 3 or n % 2 != 0:
        return 0  # No se puede expresar como suma de dos primos

    contador = 0
    for p1 in range(2, n // 2 + 1):
        if es_primo(p1):
            p2 = n - p1
            if es_primo(p2):
                contador += 1
    return contador

# Ejemplo de uso:
numero_par = 60 # Puedes cambiar este valor
formas = formas_de_sumar_primos(numero_par)
print(f"El número {numero_par} se puede expresar de {formas} maneras como suma de dos primos.")