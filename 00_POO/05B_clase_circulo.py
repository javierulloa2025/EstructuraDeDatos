class Circulo():
    pi = 3.1416 #atributo de clase
    
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.pi*self.radio*self.radio

circulo_uno = Circulo(5)
circulo_dos = Circulo(8)

print(circulo_uno.area())
print(circulo_dos.area())
