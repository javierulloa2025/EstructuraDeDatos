from claseArbol import ArbolBinario

#arbol = ArbolBinario(9)  #opc A) especificando la raíz
arbol = ArbolBinario()  #opc B) sin especificar nada, por defecto None
valores = [9, 2, 1, 16, 6, 11, 8, 4]
for valor in valores:
   arbol.insertar(valor)

print(arbol.mostrar_en_orden())
arbol.eliminar_nodo(11)
arbol.eliminar_nodo(2)
arbol.eliminar_nodo(1)
print(arbol.mostrar_en_orden())
arbol.insertar(2)
print(arbol.mostrar_en_orden())

print(arbol.localizar_elem(99))
print(arbol.localizar_elem(4))
#print(arbol.mostrar_arbol())
#arbol.inorden()
#print(" ")
#arbol.postorden()
#print(" ")
#arbol.preorden()
