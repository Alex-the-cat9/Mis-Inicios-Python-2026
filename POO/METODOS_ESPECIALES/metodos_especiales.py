class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __str__(self):
        return f"nombre:{self.nombre} edad:{self.edad}"
persona1= Persona("Alex", 15)
print(persona1)