from clase_arbol_AVL import ArbolAVL
#Ejemplo de uso
arbol = ArbolAVL()
for v in [30, 20, 40, 10, 25, 35, 50]:
    arbol = arbol.insertar(v)

print(arbol.dibujar_ascii())
arbol = arbol.eliminar_nodo(20)
print(arbol.dibujar_ascii())

print("\nPreorden tras eliminar 20:")
print(arbol.mostrar_arbol())

print(arbol.obtener_info_nodo(40))
print(arbol.dibujar_ascii())
