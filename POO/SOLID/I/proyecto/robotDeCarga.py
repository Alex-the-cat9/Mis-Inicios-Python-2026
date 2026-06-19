#RobotCarga: Este solo debe heredar de RobotBase y Caminante
import RobotBase
import Caminante
class RobotCarga(RobotBase.RobotBase, Caminante.Caminante):
    def __init__(self, nombre):
        self.nombre = nombre
    def caminar(self) -> str:
        return "RobotCarga:esta caminando"