import random

def ruleta_alumnos(lista_alumnos):
    # Hacemos una copia de la lista original para no modificarla
    alumnos_disponibles = lista_alumnos.copy()

    # Verificamos si la lista está vacía
    if not alumnos_disponibles:
        print("La lista de alumnos está vacía.")
        return

    # Mezclamos a los alumnos aleatoriamente
    random.shuffle(alumnos_disponibles)

    print("¡Bienvenido a la ruleta de alumnos!")
    print(f"Alumnos disponibles: {len(alumnos_disponibles)}")
    print("-----------------------------------")

    while alumnos_disponibles:
        input("Presiona Enter para girar la ruleta...")

        # Seleccionamos y removemos al último alumno (ya está mezclada aleatoriamente)
        alumno_seleccionado = alumnos_disponibles.pop()

        print(f"\n¡El alumno seleccionado es: {alumno_seleccionado}!")
        print(f"Alumnos restantes: {len(alumnos_disponibles)}")
        print("-----------------------------------")

    print("\n¡Todos los alumnos han sido seleccionados!")
    print("Fin del juego.")

#Uso
alumnos= ["BLANCO . DANIELA JESSICA",
"BRAVO BARRAZA GAMALIEL",
"CABRALES FRANCO JOSE",
"CASTILLO LARA JONATHAN JAVIER",
"CASTILLON CORTES OCTAVIO",
"CIAMBELLI NUÑEZ GABRIEL EDUARDO",
"DE LA CRUZ PEÑA AARON BENJAMIN",
"DELGADO GARCIA NAYELI",
"FLORES FLORES DIEGO OSCAR",
"GALLO RAMIREZ JOSUE JULIAN",
"GARCIA LUNA EDGAR OZIEL",
"GONZALEZ PAVON DANTE",
"HERMOSILLO CORRALES LEOPOLDO JAVIER",
"HERNANDEZ SALAS NATHANAEL",
"LOPEZ AGUILAR ADIN ALEJANDRO",
"MARQUEZ GUTIERREZ KAROL JIMENA",
"MARTINEZ GUERRERO EDUARDO SANTIAGO",
"MONRROY ESPINOZA DAVID ANGEL",
"ORDOÑEZ ESCOBAR ROBERTO CARLOS",
"PADILLA VELAZQUEZ VICTOR MANUEL",
"PALOMERA MILLAN RUBEN ALEJANDRO",
"PEREZ ORTEGA LUIS ALBERTO",
"RAMIREZ GUIZAR JOSE LEONARDO",
"RODRIGUEZ GARCIA JOSE ANTONIO",
"RODRIGUEZ RUVALCABA DIEGO EMMANUEL",
"SANCHEZ BECERRA ALAN ENGELBERTO",
"SANCHEZ FIGUEROA JOSE LUIS",
"SILVA HADDAD LORENZO ABRAHAM",
"SOLORZANO ESPINOSA KAISEI",
"TAPIA BARRON CESAR EMILIO",
"TERRAZAS HERNANDEZ JORGE ANDRES",
"TORRES GONZALEZ ERICK GIOVANNI",
"VALDIVIA SANTIAGO ALEJANDRO",
"VEGA CHAVEZ ANGEL FERMIN",]
ruleta_alumnos(alumnos)