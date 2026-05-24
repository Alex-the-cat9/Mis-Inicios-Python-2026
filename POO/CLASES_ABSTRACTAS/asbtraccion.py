class auto:
    def __init__(self):
        self._estado = "apagado"
    def encender(self):
        if self._estado == "apagado":
            print("auto encendido")
            self._estado = "encendido"
        else:
            print("el auto ya esta encendido")
    def conducir(self):
        if self._estado == "encendido":
            print("conduciendo")
        else:
            print("el auto esta apagado no se puede conducir")
    def apagar(self):
        if self._estado == "apagado":
            print("el auto ya estaba apagado")
        else:
            self._estado = "apagado"
            print("auto apagado")
user = auto()
while True:
    chofer = input("el auto esta apagado quisiera [encender] [conducir] [apagar] [salir]: ").lower().strip()
    if chofer == "encender":
        user.encender()
    elif chofer == "conducir":
        user.conducir()
    elif chofer == "apagar":
        user.apagar()
    elif chofer == "salir":
        break