#maestro.IA:📁 Archivo 1: conexion1.py
#(Los Núcleos de Energía - COMPONENTES)Su única responsabilidad (S):
#Programar las fuentes de poder que se meterán al chasis [INDEX_3].Tu misión:
#Crea dos clases normales independientes:ReactorNuclear: Tiene self.energia = 500.
#Tiene el método proveer_energia(self, cantidad: int) -> int que resta la cantidad y la devuelve 
#CeldaSolar: Tiene self.energia = 100. Tiene el mismo método pero solo provee energía
#si hay carga disponible Usa tus acompañantes : y -> para que mypy no te tire alertas rojas.
class ReactorNuclear:
    def __init__(self):
        self.energia = 500
    def proveer_energia(self, cantidad:int) -> int:
        aguila = self.energia - cantidad
        self.energia -= cantidad
        return aguila
class CeldaSolar:
    def __init__(self):
        self.energia = 100
    def proeveer_energia(self, cantidad:int) -> int:
        if self.energia >= cantidad:
            aguila = self.energia - cantidad
            return aguila
        else:
            raise ValueError("sin energia")
        

