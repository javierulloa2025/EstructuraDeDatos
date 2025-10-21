"""mejora el código manteniendo las letras que sean correctas y 
modificando sólo un carácter en la mejor secuencia hasta el momento. 
Esto para hacerlo del tipo hill climbing, es decir, 
solo mantenemos el resultado si es mejor que el anterior"""

import random
import string

def generar_frase_mejorada(mejor_frase_actual, frase_objetivo):
    """
    Genera una nueva frase basada en la mejor actual, modificando solo un carácter incorrecto.
    """
    # Si es la primera iteración, generar una frase completamente aleatoria
    if not mejor_frase_actual:
        caracteres = string.ascii_letters + string.digits + " .,!?;:'\"-"
        return ''.join(random.choice(caracteres) for _ in range(len(frase_objetivo)))
    
    # Encontrar posiciones de caracteres incorrectos
    posiciones_incorrectas = []
    for i, (actual, objetivo) in enumerate(zip(mejor_frase_actual, frase_objetivo)):
        if actual != objetivo:
            posiciones_incorrectas.append(i)
    
    # Si ya está todo correcto, retornar la misma frase
    if not posiciones_incorrectas:
        return mejor_frase_actual
    
    # Elegir una posición incorrecta aleatoria para modificar
    posicion_a_cambiar = random.choice(posiciones_incorrectas)
    
    # Generar nuevo carácter para esa posición
    caracteres = string.ascii_letters + string.digits + " .,!?;:'\"-"
    nuevo_caracter = random.choice(caracteres)
    
    # Construir nueva frase manteniendo los caracteres correctos
    nueva_frase = list(mejor_frase_actual)
    nueva_frase[posicion_a_cambiar] = nuevo_caracter
    
    return ''.join(nueva_frase)

def calificar_frase(frase_generada, frase_objetivo):
    """
    Evalúa qué porcentaje de caracteres son correctos.
    Retorna el porcentaje y una lista con los caracteres correctos.
    """
    correctos = 0
    caracteres_correctos = []
    
    for gen, obj in zip(frase_generada, frase_objetivo):
        if gen == obj:
            correctos += 1
            caracteres_correctos.append(gen)
        else:
            caracteres_correctos.append('_')
    
    porcentaje = (correctos / len(frase_objetivo)) * 100
    return porcentaje, ''.join(caracteres_correctos), correctos

def simular_mono_hill_climbing(frase_objetivo):
    """
    Simula el teorema del mono usando algoritmo Hill Climbing.
    Mantiene los caracteres correctos y solo modifica uno incorrecto por iteración.
    """
    longitud = len(frase_objetivo)
    mejor_porcentaje = 0
    mejor_frase = ""
    mejor_correctos = 0
    intentos = 0
    iteraciones_sin_mejora = 0
    
    print(f"Frase objetivo: '{frase_objetivo}'")
    print(f"Longitud: {longitud} caracteres")
    print("Algoritmo: Hill Climbing (mantiene caracteres correctos)")
    print("=" * 60)
    
    # Generar frase inicial
    frase_actual = generar_frase_mejorada("", frase_objetivo)
    porcentaje_actual, frase_correcta, correctos_actual = calificar_frase(frase_actual, frase_objetivo)
    
    mejor_porcentaje = porcentaje_actual
    mejor_frase = frase_actual
    mejor_correctos = correctos_actual
    
    print(f"Frase inicial: '{frase_correcta}' ({porcentaje_actual:.2f}%)")
    
    while True:
        intentos += 1
        
        # Generar nueva frase basada en la mejor actual
        nueva_frase = generar_frase_mejorada(mejor_frase, frase_objetivo)
        
        # Calificar la nueva frase
        porcentaje_nuevo, frase_correcta_nueva, correctos_nuevo = calificar_frase(nueva_frase, frase_objetivo)
        
        # Aceptar la nueva frase solo si es mejor o igual (permite movimientos laterales)
        if correctos_nuevo >= mejor_correctos:
            if correctos_nuevo > mejor_correctos:
                iteraciones_sin_mejora = 0
                print(f"🎯 Mejora en intento #{intentos}: '{frase_correcta_nueva}' ({porcentaje_nuevo:.2f}%)")
            else:
                iteraciones_sin_mejora += 1
            
            mejor_porcentaje = porcentaje_nuevo
            mejor_frase = nueva_frase
            mejor_correctos = correctos_nuevo
        
        # Mostrar progreso cada 1000 intentos
        if intentos % 1000 == 0:
            _, mejor_frase_visual, _ = calificar_frase(mejor_frase, frase_objetivo)
            print(f"\n📊 Progreso en intento #{intentos:,}")
            print(f"Mejor frase: '{mejor_frase_visual}'")
            print(f"Porcentaje: {mejor_porcentaje:.2f}%")
            print(f"Iteraciones sin mejora: {iteraciones_sin_mejora}")
            print("-" * 40)
        
        # Verificar si se encontró la frase completa
        if mejor_porcentaje == 100:
            print("\n" + "🎉" * 25)
            print("¡ÉXITO! Se encontró la frase completa.")
            print(f"Frase encontrada: '{mejor_frase}'")
            print(f"Total de intentos: {intentos:,}")
            print("🎉" * 25)
            break
        
        # Estrategia de reinicio si se estanca
        if iteraciones_sin_mejora > 5000:
            print(f"\n🔄 Reiniciando búsqueda (estancado por {iteraciones_sin_mejora} iteraciones)")
            # Mantenemos algunos caracteres correctos aleatoriamente
            nueva_base = list(mejor_frase)
            caracteres_a_mantener = random.randint(1, mejor_correctos // 2)
            
            posiciones_correctas = [i for i, (a, b) in enumerate(zip(mejor_frase, frase_objetivo)) if a == b]
            if posiciones_correctas:
                posiciones_a_eliminar = random.sample(posiciones_correctas, min(caracteres_a_mantener, len(posiciones_correctas)))
                for pos in posiciones_a_eliminar:
                    caracteres = string.ascii_letters + string.digits + " .,!?;:'\"-"
                    nueva_base[pos] = random.choice(caracteres)
            
            mejor_frase = ''.join(nueva_base)
            mejor_porcentaje, _, mejor_correctos = calificar_frase(mejor_frase, frase_objetivo)
            iteraciones_sin_mejora = 0
            print(f"Nueva base: '{mejor_frase}' ({mejor_porcentaje:.2f}%)")

def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    print("🐒 SIMULADOR DEL TEOREMA DEL MONO - HILL CLIMBING 🐒")
    print("=" * 60)
    print("Estrategia: Mantiene caracteres correctos, modifica solo 1 incorrecto por iteración")
    print("=" * 60)
    
    while True:
        frase = input("\nIngresa la frase a generar (o 'salir' para terminar): ")
        
        if frase.lower() == 'salir':
            print("¡Hasta luego!")
            break
        
        if not frase.strip():
            print("Por favor, ingresa una frase válida.")
            continue
        
        print("\nIniciando simulación con Hill Climbing...")
        simular_mono_hill_climbing(frase)

if __name__ == "__main__":
    main()