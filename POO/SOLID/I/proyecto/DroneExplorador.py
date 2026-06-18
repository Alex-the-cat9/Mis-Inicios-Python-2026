import RobotBase
import volador
#DroneExplorador: Este solo debe heredar de RobotBase y Volador
class DroneExplorador(RobotBase.RobotBase, volador.Volador):
    def __init__(self, nombre):
        self.nombre = nombre
    def Volar(self) -> str:
        return "DRONEexplorador:esta volando"
    
        