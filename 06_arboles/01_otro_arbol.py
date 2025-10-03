from claseArbol import ArbolBinario

a = ArbolBinario()

valores = [5, 4, 1, 3, 3, 4,9]
for valor in valores:
   a.insertar(valor)

print(a.mostrar_en_orden())