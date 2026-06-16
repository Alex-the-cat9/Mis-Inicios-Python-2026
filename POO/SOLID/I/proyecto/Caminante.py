import abc
class Caminante(abc.ABC):
    @abc.abstractmethod
    def caminar(self) -> str:
        pass