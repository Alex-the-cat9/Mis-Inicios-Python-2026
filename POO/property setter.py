class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def calcular(self):
        calculo = 100 - self.__edad
        print(f"faltan {calculo} años para los 100 años")
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nuevo):
        self.__nombre = nuevo
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, nuevo):
        self.__edad = nuevo
aguila = Persona("PEPE", 10)
nombre = aguila.nombre
print(nombre)
aguila.nombre = "Alex"
aguila.edad = 15
nombre,edad = aguila.nombre, aguila.edad
print(f"nombre del nuevo:{nombre} edad del nuevo:{edad}")
aguila.calcular()