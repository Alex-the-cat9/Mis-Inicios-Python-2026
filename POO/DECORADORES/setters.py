class Telefono:
    def __init__(self):
        self.__PRIVACIDAD = "Alex-the-cat9"
    def set_privacidad(self):
        self.__PRIVACIDAD = "Alex"
        return self.__PRIVACIDAD
tele = Telefono()
aguila = tele.set_privacidad()
print(aguila)
