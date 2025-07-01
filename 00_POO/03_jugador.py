class Jugador():

    #Atributos
    edad = None

    #Métodos
    def permitir_acceso(self):
        print("acceso permitido")

    def denegar_acceso(self):
        print("acceso denegado")

    def comprobar_edad(self):
        if self.edad < 18:
            self.denegar_acceso()
        else:
            self.permitir_acceso()

juan = Jugador()

juan.edad = int(input("Dime tu edad: "))
juan.comprobar_edad()

