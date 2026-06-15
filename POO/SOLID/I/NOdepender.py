import abc
class Humano(abc.ABC):
    def __init__(self, nombre:str, edad:int, empleo:str) -> None:
        pass
    @abc.abstractmethod
    def comer(self):
        pass
    @abc.abstractmethod
    def dormir(self):
        pass
    @abc.abstractmethod
    def trabajar(self):
        pass
class humano(Humano):
    def __init__(self, nombre:str, edad:int, empleo:str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.empleo = empleo
    def comer(self):
        print(f"{self.nombre}:esta comiendo")
    def dormir(self):
        print(f"{self.nombre}: esta durmiendo")
    def trabajar(self):
        print(f"{self.nombre}:esta trabajando De {self.empleo}")
Alex = humano("Alex", 15, "programador")
Alex.comer()
Alex.dormir()
Alex.trabajar()
print("Robot esta trizte no ay una clase padre para que el pueda vivir y la unica que ay es para humanos robot no come no duerme")
print("crearemos una clase padre para el")
class Robot(abc.ABC):
    def __init__(self, nombre:str) -> None:
        pass
    def ayudar(self):
        pass
    def programar(self):
        pass
    def investigar(self):
        pass
class IA(Robot):
    def __init__(self, nombre:str) -> None:
        self.nombre = nombre
    def ayudar(self):
        print(f"{self.nombre}: te esta ayudando")
    def programar(self):
        print(f"{self.nombre}: te esta programando")
    def investigar(self):
        print(f"{self.nombre}:esta investigando")
inteligencia_artificial = IA("IA")
inteligencia_artificial.ayudar()
inteligencia_artificial.programar()
inteligencia_artificial.investigar()

        
