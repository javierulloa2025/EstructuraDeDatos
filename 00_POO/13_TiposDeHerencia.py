#Tipos de herencia en Python
# 1)Herencia simple
class A():
    pass

class B(A):  # La clase B, herera de A
    pass

#Herencia múltiple: una clase recibe herencias de varias superclases
class A(object):  #la clase "object" indica que la clase no hereda de otra, es opcional pero recomendado
    pass
class B(object):
    pass
class C(object):
    pass

class D(A, B, C):  #la clase D hereda de las superclases A, B y C
    pass

#Herencia multinivel: Son clases que van heredando en varios niveles 
class A(object):
    pass
class B(A):
    pass
class C(B):
    pass
class D(C):  #la clase D hereda de la superclase C que a su vez hereda de B...
    pass


#Método mro: indica el camino o ruta de herencia de una clase

print(D.mro())  #ejemplo: salida [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

#Herencia jerarquica: existe una clase principal y varias clases secundarias o sub que heredan de la misma superclase
class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass

#Herencia hibrida o mixta
# Mezcla de diferentes herencias (se puede complicar sino se hace un diagrama)



