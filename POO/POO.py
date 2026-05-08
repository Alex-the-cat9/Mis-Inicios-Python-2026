import sys
class estudiante():
    def __init__(self,nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    def estudiar(self):
        print(F"el estudiante {self.nombre} esta estudiando")
try:
    nombre = input("diga su nombre: ")
    edad = int(input("diga su edad solo numero: "))
    grado = input("digame su grado: ")
except ValueError:
    print("era solo numeros")
    sys.exit()
else:
    estudiante1 = estudiante(nombre, edad, grado)
    estudiar = input("desea estudiar?[si] [no]: ").lower()
    if estudiar == "si":
        estudiante1.estudiar()
    else:
        print(f"burro:{estudiante1.nombre}")
