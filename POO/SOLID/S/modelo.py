class Personaje:
    def __init__(self,nombre,poder):
          self.nombre = nombre
          self.poder = poder
    def  __repr__(self):
         return f"nombre:{self.nombre} poder:{self.poder}"
    def __str__(self):
         return f"nombre:{self.nombre} poder:{self.poder}"
    def __add__(self, other):
         nombre = self.nombre[0:2] + other.nombre[2:]
         poder = self.poder + other.poder
         return Personaje(nombre, poder)