import abc
class Motor(abc.ABC):
    @abc.abstractmethod
    def prender(self):
        pass
class Motor_baja(Motor):
    def __init__(self):
        pass
    def prender(self):
        print("Motor calidad baja prendida")
class Motor_media(Motor):
    def __init__(self):
        pass
    def prender(self):
        print("motor media prendido de calidad media")
class Motor_Alta(Motor):
    def __init__(self):
        pass
    def prender(self):
        print("Motor de gama Alta prendido")
class Mi_auto:
    def __init__(self, motor:Motor):
        self.motor = motor
    def conducir(self):
        self.motor.prender()
print("1:motor calidad baja")
print("2:motor calidad media")
print("3:motor calidad alta")
while True:
    try:
        user = int(input("elige con un numero que motor quieres: "))
    except ValueError:
        print("era un numero")
    else:
        break
if user == 1:
    calidad = Motor_baja()
    primer_auto = Mi_auto(calidad)
elif user == 2:
    calidad_media = Motor_media()
    primer_auto = Mi_auto(calidad_media)#mypy dijo que no puedop usar la misma variable:(
else:
    calidad_alta = Motor_Alta()
    primer_auto = Mi_auto(calidad_alta)
primer_auto.conducir()