from clase_arbol_AVL import ArbolAVL

arbol3 = ArbolAVL()

arbol3 = arbol3.insertar(12)
arbol3 = arbol3.insertar(14)
arbol3 = arbol3.insertar(8)
arbol3 = arbol3.insertar(6)
arbol3 = arbol3.insertar(9)
print(arbol3.dibujar_ascii())
arbol3 = arbol3.insertar(10)
print(arbol3.dibujar_ascii())

