from abc import ABC, abstractmethod
from pydantic import Field, BaseModel
from hashlib import sha256
class Usuario(BaseModel):
    Name:str = Field(min_length=2)
    Password:str = Field(min_length=4)
class User_comon(ABC):
    @abstractmethod
    def Inicio_sesion(self, User:Usuario):
        pass
    @abstractmethod
    def registrar(self, User:Usuario) -> bool | str:
        pass
class System(User_comon):
    def __init__(self):
        self.__base = {}
    def Inicio_sesion(self, User:Usuario):
        if User.Name.casefold() not in self.__base:
            return False
        salt = sha256(User.Password.encode()).hexdigest()
        for i in self.__base[User.Name.casefold()]:
            if salt == i["Contraseña"]:
                return "Bienvenido"
            else:
                return False
    def registrar(self, User:Usuario) -> bool | str:
        if User.Name.casefold() in self.__base:
            return False
        salt = sha256(User.Password.encode()).hexdigest()
        self.__base[User.Name.casefold()] = [{"Contraseña":salt}]
        return "bienvenido"
if __name__ == "__main__":
    #probar registrar
    systema = System()
    Identificador = Usuario(Name="Alex", Password="1001112")
    User1 = systema.registrar(Identificador)
    print(f"el registro fue un exito:{User1}")
    #probar iniciar sesion
    inicio_sesion = systema.Inicio_sesion(Identificador)
    print(f"El inicio de sesion fue un exito:{inicio_sesion}")
    #probar mas registros y inicios de sesion
    Identificador1 = Usuario(Name="Juan", Password="xd12")
    Identificador2 = Usuario(Name="pedro", Password="122112")
    Identificador3 = Usuario(Name="perro", Password="1010101")
    User2 = systema.registrar(Identificador1)
    User3 = systema.registrar(Identificador2)
    User4 = systema.registrar(Identificador3)
    inicio_sesion1 = systema.Inicio_sesion(Identificador1)
    inicio_sesion2 = systema.Inicio_sesion(Identificador2)
    inicio_sesion3 = systema.Inicio_sesion(Identificador3)
    print(f"El inicio de sesion de juan fue un exito:{inicio_sesion1}")
    print(f"El inicio de sesion de pedro fue un exito:{inicio_sesion2}")
    print(f"El inicio de sesion de perro fue un exito:{inicio_sesion3}")
    #probar anti nombres duplicados
    Identificador0 = Usuario(Name="Juan", Password="xd12")
    User0 = systema.registrar(Identificador0)
    print(f"se detuvo a juan por ser un nombre duplicado(si dice false entonces si fue un nombre duplicado): {User0}")
    #probar contraseñas incorrectas
    Identificador4 = Usuario(Name="Juan", Password="XD12")
    User4 = systema.Inicio_sesion(Identificador4)
    print(f"se detuvo a juan por intentar poner una contraseña incorrecta (si dice false entonces si fue una contraseña incorrecta): {User4}")