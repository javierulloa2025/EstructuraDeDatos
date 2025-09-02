"""El módulo pickle en Python se utiliza para serializar y deserializar objetos Python, 
convirtiéndolos en una secuencia de bytes que se puede guardar en un archivo o transmitir por red. 
La deserialización reconstruye el objeto a partir de la secuencia de bytes"""

import pickle

datos = {"nombre": "Francisco", "edad": 45}

with open("datos.pkl", "wb") as f:
    pickle.dump(datos, f)

with open("datos.pkl", "rb") as f:
    datos_cargados = pickle.load(f)

print(datos_cargados)