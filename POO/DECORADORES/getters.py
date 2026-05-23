class Persona:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.__edad = edad
    def dad(self):
        return self.__edad
persona = Persona("pepe", 999)
aguila = persona.dad()
print(aguila)
