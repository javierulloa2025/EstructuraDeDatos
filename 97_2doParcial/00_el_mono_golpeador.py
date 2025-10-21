"""Prompt: Crea un programa en Python, que simule el teorema del mono golpeando teclas, 
el programa recibe una frase a generar; 
luego aleatoriamente genera frases de la longitud de la frase ingresada, 
otra función evalúa el resultado mediante comparación; 
una tercera función llamará repetitivamente a las funciones generar y calificar, 
terminará si el 100% de las letras son correctas; 
si las letras no son correctas, se generará una nueva cadena completa, 
para dar seguimiento al programa, 
otra función deberá imprimir la mejor secuencia generada hasta el momento y 
su calificación correspondiente cada 1000 intentos."""

import random
import string

def generar_frase(longitud):
    """
    Genera una frase aleatoria de la longitud especificada.
    Incluye letras mayúsculas, minúsculas, espacios y signos de puntuación básicos.
    """
    caracteres = string.ascii_letters + string.digits + " .,!?;:'\"-"
    return ''.join(random.choice(caracteres) for _ in range(longitud))

def calificar_frase(frase_generada, frase_objetivo):
    """
    Evalúa qué porcentaje de caracteres son correctos.
    Retorna el porcentaje y una lista con los caracteres correctos.
    """
    correctos = 0
    caracteres_correctos = []
    
    for i, (gen, obj) in enumerate(zip(frase_generada, frase_objetivo)):
        if gen == obj:
            correctos += 1
            caracteres_correctos.append(gen)
        else:
            caracteres_correctos.append('_')
    
    porcentaje = (correctos / len(frase_objetivo)) * 100
    return porcentaje, ''.join(caracteres_correctos)

def simular_mono(frase_objetivo):
    """
    Simula el teorema del mono infinito generando frases aleatorias
    hasta encontrar la frase objetivo.
    """
    longitud = len(frase_objetivo)
    mejor_porcentaje = 0
    mejor_frase = ""
    intentos = 0
    
    print(f"Frase objetivo: '{frase_objetivo}'")
    print(f"Longitud: {longitud} caracteres")
    print("=" * 50)
    
    while True:
        # Generar nueva frase
        frase_actual = generar_frase(longitud)
        intentos += 1
        
        # Calificar la frase generada
        porcentaje_actual, frase_correcta = calificar_frase(frase_actual, frase_objetivo)
        
        # Actualizar la mejor frase si es necesario
        if porcentaje_actual > mejor_porcentaje:
            mejor_porcentaje = porcentaje_actual
            mejor_frase = frase_correcta
        
        # Mostrar progreso cada 1000 intentos
        if intentos % 1000 == 0:
            print(f"Intento #{intentos:,}")
            print(f"Mejor frase hasta ahora: '{mejor_frase}'")
            print(f"Porcentaje correcto: {mejor_porcentaje:.2f}%")
            print("-" * 30)
        
        # Verificar si se encontró la frase completa
        if porcentaje_actual == 100:
            print("\n" + "🎉" * 20)
            print("¡ÉXITO! Se encontró la frase completa.")
            print(f"Frase encontrada: '{frase_actual}'")
            print(f"Total de intentos: {intentos:,}")
            print("🎉" * 20)
            break
            
        # Opcional: agregar un límite de intentos para evitar bucles infinitos muy largos
        if intentos > 10000000:
            print("\nSe alcanzó el límite de 10,000,000 intentos.")
            print(f"Mejor resultado obtenido: '{mejor_frase}' ({mejor_porcentaje:.2f}%)")
            break

def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    print("🐒 SIMULADOR DEL TEOREMA DEL MONO INFINITO 🐒")
    print("=" * 50)
    
    while True:
        frase = input("\nIngresa la frase a generar (o 'salir' para terminar): ")
        
        if frase.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if not frase.strip():
            print("Por favor, ingresa una frase válida.")
            continue
        
        print("\nIniciando simulación...")
        simular_mono(frase)

if __name__ == "__main__":
    main()