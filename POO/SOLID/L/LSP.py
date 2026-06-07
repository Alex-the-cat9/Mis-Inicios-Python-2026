#📡 TU INFORME DE INTELIGENCIA (Tu Misión)Si tu archivo principal main.py está diseñado esperando que todas las baterías
#del imperio se recarguen igual (es decir, metiendo corriente eléctrica en horizontal con un solo número: bateria.recargar(50))
#¿qué va a pasar en la memoria RAM en el milisegundo en que el chofer intente usar la BateriaBunkerMilitar?
#Analiza el script en tu libreta y respóndeme con la ley marcial en la mano :¿Qué letras rojas de error va a escupir la PowerShell
#de Windows por culpa de la firma del método del Hijo 2 ?¿Por qué este diseño obliga de forma corrupta
#a modificar el main.py, rompiendo la O y la L al mismo tiempo ?
import abc

# 🏛️ El Plano de Hierro (CERRADO e intocable)
class BateriaBase(abc.ABC):
    @abc.abstractmethod
    def recargar(self, cantidad):
        pass

# 🧬 Hijo 1: Cumple las leyes perfectamente
class BateriaCelular(BateriaBase):
    def __init__(self):
        self.energia = 50
        
    def recargar(self, cantidad):
        self.energia += cantidad
        if self.energia > 100:
            self.energia = 100

# 🚨 Hijo 2: EL SOSPECHOSO DE SABOTAJE MOLECULAR
class BateriaBunkerMilitar(BateriaBase):
    def __init__(self):
        self.energia = 1000
        self.bloqueada = False
        
    def recargar(self, cantidad, codigo_seguridad):#siento que el problema es codiogo_seguridad
        if codigo_seguridad == "1234":
            self.energia += cantidad
        else:
            raise ValueError("Acceso denegado")
