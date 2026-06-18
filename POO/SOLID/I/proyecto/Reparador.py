import abc
class Reparador(abc.ABC):
    @abc.abstractmethod
    def Reparar(self) -> str:
        pass