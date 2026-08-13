from pydantic import Field, BaseModel, ValidationError
from typing import Final
class usuario(BaseModel):
    username:str = Field(min_length=2, max_length=10)
    password:str = Field(min_length=3)
class system:
    def __init__(self):
        self.__system:dict[str, str] = {}
    def añadir_user(self, Usuario:usuario):
        if Usuario.username in self.__system:
            return False
        if Usuario.username not in self.__system:
            self.__system[Usuario.username] = Usuario.password
            return "esta dentro"
    def votar_user(self, Usuario:str):
        if Usuario in self.__system:
            del self.__system[Usuario]
            print("ya fue eliminado")
        else:
            return False
if __name__ == "__main__":
    System = system()
    new_user = usuario(username="Alex", password="1202")
    user1 = System.añadir_user(new_user)
    print(user1)
    user2 = System.añadir_user(new_user)
    if user2:
        print("True")
    else:
        print("False")
    System.votar_user("Alex")
    #pruebas
    try:
        new_use = usuario(username="A", password="1202")
        System.añadir_user(new_user)
    except ValidationError:
        print("alguien intento entrar con nombre corto")
    else:
        print("Ups")

