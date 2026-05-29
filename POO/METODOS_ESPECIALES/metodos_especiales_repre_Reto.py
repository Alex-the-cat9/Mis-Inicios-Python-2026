#🩻 Las Especificaciones del Desafío: El Saco de ClonesVas a crear una clase llamada ComponenteIA
#Queremos que cuando guardemos múltiples componentes adentro de una lista [] y hagamos un print(), la terminal de Windows no nos tire el
#texto gris de los juniors, sino la radiografía exacta de sus ingredientes .⚠️ Las 2 Únicas Reglas del Circuito:El Constructor:
#En el __init__, guarda el nombre del chip en self.chip y su voltaje en self.voltios .El Gemelo de Bolsillo (__repr__):
#Programa el método especial def __repr__(self): para que devuelva con un return la receta exacta en este formato de texto:
#"ComponenteIA(chip='{self.chip}', voltios={self.voltios})"
class ComponenteIA:
    def __init__(self):
        self.chip = 30
        self.voltios = 50
    def __repr__(self):
        return f"ComponenteIA(chip='{self.chip}', voltios={self.voltios})"
IA = ComponenteIA()
print(repr(IA))