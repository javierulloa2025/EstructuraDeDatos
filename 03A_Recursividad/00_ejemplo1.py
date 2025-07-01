#Contar páginas de varios libros

#Solución iterativa:
"""
libros = [50, 100, 150, 70, 250]
total = 0
for libro in libros:
    total+= libro

print(total) #salida 620
"""

#Solución recursiva

def total_paginas(libros):
    if len(libros) == 1:
        return libros[0]
    else: 
        return libros[0] + total_paginas(libros[1:])
    
print(total_paginas([50, 100, 150]))

