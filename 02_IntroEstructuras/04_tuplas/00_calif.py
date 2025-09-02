reporte = (
           ("Juan",[90,60,70,100]), 
           ("Ana", [100, 85, 60, 85]),
           ("Pedro", [90, 100, 100, 100]),
           ("Ramón", [90, 95, 100, 100]),
           ("María", [100, 85, 100, 90])
           )
          
for estudiante, calificaciones in reporte:
    promedio = sum(calificaciones) / len(calificaciones)
    print(f"{estudiante}, promedio: {promedio}")
    