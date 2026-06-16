#AndroideIngeniero: Este es un híbrido; debe heredar de RobotBase, Caminante y Reparador
import RobotBase
import Caminante
import Reparador
class AndroideIngeniero(RobotBase.RobotBase, Caminante.Caminante, Reparador.Reparador):
    def __init__(self, nombre):
        self.nombre = nombre
    def caminar(self) -> str:
        return "AndroideIngeniero:esta caminando"
    def Reparar(self) -> str:
        return "androideingeniero:esta reparando"
    
        