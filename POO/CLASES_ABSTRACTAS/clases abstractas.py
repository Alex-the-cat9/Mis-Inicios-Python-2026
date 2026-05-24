from abc import ABC, abstractclassmethod
class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, genero, actividad):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.actividad = actividad

    def presentarse(self):
        print(f"hola me llamo:{self.nombre} tengo {self.edad} años")
class Estudiante(Persona):
    def __init__(self, nombre, edad, genero, actividad):
        super().__init__(nombre, edad, genero, actividad)
    def hacer_actividad(self):
        print(f"estoy estudiando: {self.actividad}")
    def presentarse(self):
        return super().presentarse()
class trabajador(Persona):
    def __init__(self, nombre, edad, genero, trabajar):
        super().__init__(nombre, edad, genero, trabajar)
    def hacer_actividad(self):
        print(f"estoy trabajando: {self.actividad}")
    def presentarse(self):
        return super().presentarse()
Alex = Estudiante("Alex", 15, "masculino", "programador")
Alex.presentarse()
Alex.hacer_actividad()
IA = trabajador("IA", 30, "IA", "Inteligencia artificial")
IA.presentarse()
IA.hacer_actividad()