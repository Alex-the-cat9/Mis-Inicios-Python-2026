#📁 Archivo 1: conexion1.py
#(La Bóveda del Contrato - PADRE) Su única responsabilidad (S):
#Definir el ADN y las leyes abstractas del imperio Tu misión: Crea la clase abstracta TorretaBase(abc.ABC)
#Diseña el método abstracto obligatorio def disparar(self, rafaga: int) -> str:.La Ley de la L (Acompañantes):
#Obliga a que la entrada sea sí o sí un entero (rafaga: int) y promete que la salida será un texto plano (-> str)
#¡Prohibido meter lógica o prints aquí!
import abc
class TorretaBase(abc.ABC):
    @abc.abstractmethod
    def disparar(self, rafaga:int) -> str:
        pass