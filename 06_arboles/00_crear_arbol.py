from claseArbol import ArbolBinario

#arbol1 = ArbolBinario(9)  #opc A) especificando la raíz
arbol = ArbolBinario() 

valores = [8, 3, 1, 20, 5, 10, 7, 4,22,33,41]

for valor in valores:
   arbol.insertar(valor)

print(arbol.mostrar_en_orden())
print(arbol.mostrar_arbol())

print(f"La altura es: {arbol.altura_arbol()}")

"""
print(arbol.buscar(8)) #True
print(arbol.buscar(99)) #False

print(arbol.altura_arbol())

min = arbol.encontrar_min()
max = arbol.encontrar_max()
print(min.valor)
print(max.valor)"""