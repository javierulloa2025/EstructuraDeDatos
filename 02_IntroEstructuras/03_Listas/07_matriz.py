matriz = [
          [1, 2,  3],
          [4, 5,  6],
          [7, 8,  9],
          [10,11,12],
                           ]
for i in range(len(matriz)): #recorre las filas
    for j in range (len(matriz[0])): #recorre las columnas
       print(f"El elemento en fila {i+1}, columna {j+1}: {matriz[i][j]}")
