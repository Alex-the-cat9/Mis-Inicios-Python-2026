#🩻 Las Especificaciones del Desafío: La Amperaje TotalVas a crear una clase llamada NucleoEnergia
#Queremos que cuando sumes dos núcleos usando el signo más (+), la RAM los funda en un tercer núcleo totalmente nuevo que contenga
#el total de los amperios combinados Las 2 Únicas Reglas del Circuito:El Constructor: En el __init__, guarda los amperios
#en el casillero self.amperiosl Interruptor del Signo Más (__add__): Programa el método especial def __add__(self, otro):
#Debe sumar self.amperios más outro.amperios y, usando un return, fabricar y devolver un NUEVO objeto NucleoEnergia con ese poder tota
class NucleoEnergia:
    def __init__(self, imperio1):
        self.imperio1 = imperio1
    def __add__(self, other):
        nuevo = self.imperio1 + other.imperio1
        return nuevo
nucleo = NucleoEnergia("michi")
nucleo2 = NucleoEnergia("perros")
print("tregua")
nuevo = nucleo + nucleo2
print(f"el imperio mas grande de todos el nuevo:{nuevo}")