#crear un sistema para la escuela En este sistema, Vamos a tener dos clases principales:
#persona y estudiante. La clase persona tendra los atributos de nombre y edad y un metodo que imprima el nombre
#y la edad de la persona. La clase estudiante heredara de la clase Persona y tambien tendra un atributo adicional:
#grado  y un metodo que imprima el grado del estudiante.

#Deberas utilizar super en el metodo inicializacion (init) para reutilizar el codigo de la clase padre
#(Persona). Luego crea una instancia de la clase estudiante e imprime sus atributos y utiliza sus metodos 
#para asegurarte de que todo funcione correctamente.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar(self):
        print(f"Nombre:{self.nombre}")
        print(f"edad:{self.edad}")
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    def gradoEstudiante(self):
        print(f"Grado:{self.grado}")
estudiante1 = Estudiante("Roberto", 15, "secundaria")
estudiante1.mostrar()
estudiante1.gradoEstudiante()