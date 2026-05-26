#Alex:repr es el hermano gemelo de str pero mas desordenado
class Detectar_Virus:
    def __init__(self):
        self.nombre = "Alex"
        self.virus = ["MALWARE", "TROYAN"]
    def __str__(self):
        return f"{self.nombre} AY VIRUS:{self.virus}"
    def __repr__(self):
        return f"{self.nombre} AY VIRUS:{self.virus}"
anti_virus = Detectar_Virus()
print(anti_virus)
print(repr(anti_virus))

lista_prueba = [anti_virus]
print(lista_prueba)