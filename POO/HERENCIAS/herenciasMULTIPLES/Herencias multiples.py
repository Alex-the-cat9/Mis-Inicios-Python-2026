class persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    def hablar(self):
        print("HOLA CARAJOOO")
    def presentarse(self):
        print("PERSONA COMUN:")
        print(f"nombre:{self.nombre}")
        print(f"edad:{self.edad}")
        print(f"nacionalidad:{self.nacionalidad}")
class Estudiante(persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas = notas
        self.universidad = universidad
    def presentarse(self):
        print("ESTUDIANTE:")
        print(f"nombre:{self.nombre}")
        print(f"edad:{self.edad}")
        print(f"nacionalidad:{self.nacionalidad}")
        print(f"notas:{self.notas}")
        print(f"universidad:{self.universidad}")
class artista:
    def __init__(self,habilidad):
        self.habilidad = habilidad
    def habilida(self):
        print(f"mi habilidad es:{self.habilidad}")
persona_comun = persona("juan", 21, "españa")
persona_comun.presentarse()
class estudiante_artista(Estudiante,artista):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad, habilidad, perfeccion):
        Estudiante.__init__(self,nombre,edad,nacionalidad,notas,universidad)
        artista.__init__(self,habilidad)
        self.perfeccion = perfeccion
    def presentarse(self):
        print("ESTUDIANTE SUPREMO: ")
        print(f"NOMBRE:{self.nombre}")
        print(f"edad:{self.edad}")
        print(f"nacionalidad:{self.nacionalidad}")
        print(f"notas:{self.notas}")
        print(f"universidad:{self.universidad}")
        print(f"habilidad:{self.habilidad}")
        print(f"perfeccion:{self.perfeccion}")
estudiante_supremo = estudiante_artista("ALEX", 15, "PERU","10/10", "UTP", "PROGRAMACION", "INTELIGENCIA_ALTA")
estudiante_supremo.presentarse()

        
