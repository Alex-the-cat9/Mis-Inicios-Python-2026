import abc
class Volador(abc.ABC):
    @abc.abstractmethod
    def Volar(self) -> str:
        pass