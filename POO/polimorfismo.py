class Perro:
    def sonido(self):
        print("GUAU")
class Gato:
    def sonido(self):
        print("MIAU")
class Humano:
    def sonido(self):
        print("Hola")
class Gallo:
    def sonido(self):
        print("sonido de gallo")
perro = Perro()
gato = Gato()
humano = Humano()
gallo = Gallo()
sonidos = [perro, gato, humano, gallo]
for i in sonidos:
    i.sonido()