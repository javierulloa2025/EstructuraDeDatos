lista = [1, 1, 1, 1] #True
lista2 = [1, 2, 3, 2] #False

milistaunica = list(set(lista2))
if len(milistaunica) <= 1:
    print(True)
else:
    print(False)
    