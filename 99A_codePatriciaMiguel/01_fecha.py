"""
Fecha a procesar, con formato ddmmaaaa o dmmaaaa 
(donde las "d" indican los dígitos del día, las "m" indican los dígitos del mes y las "a" 
indican los dígitos del año). Positivo.
"""

def buscar_mes(fecha):
    return int(str(fecha)[2:4])
    
buscar_mes(fecha=31122020)
print(buscar_mes(fecha=31122020))