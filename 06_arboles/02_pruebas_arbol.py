from claseArbol import ArbolBinario

ar = ArbolBinario(9)
ar.insertar(1)
ar.insertar(11)


minimo = ar.encontrar_min()
maximo = ar.encontrar_max()
print(minimo.valor)
print(maximo.valor)
ar.eliminar_nodo(1)
print(ar.mostrar_arbol())
print(minimo.valor)





