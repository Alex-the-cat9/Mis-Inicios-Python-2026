from hashlib import sha256
from pydantic import BaseModel, Field, ValidationError
from fastapi import FastAPI
from typing import Final
import json
class Usuari(BaseModel):
    nombre:str = Field(min_length=2)
    Password:str = Field(min_length=4)
app = FastAPI()
Errores = {
    "User":"el nombre deve tener un minimo de 2 caracteres",
    "Password":"La contraseña deve tener un minimo de 4 caracteres",
    "repetido":"el nombre ya esta dentro del servidor",
    "no-existe":"el nombre que puso no existe en el servidor"
}
Base = {}
try:
    with open("server.json", "r") as f:
        Base = json.load(f)
except FileNotFoundError:
    with open("server.json", "w", encoding="utf-8") as f:
        json.dump(Base, f, indent=4, ensure_ascii=False)
def actualizar():
    with open("server.json", "w", encoding="utf-8") as f:
        json.dump(Base, f, indent=4, ensure_ascii=False)
class System:
    def __init__(self):
        self.__Base = {}
    def enviar_datos(self):
        return self.__Base
    def recibir_datos(self, User:dict):
        for i in User:
            if User[i]["revelacion"] == "rechazado":
                return Errores.get(
                    User[i]["causa"],
                    "parece que estamos teniendo errores desconocidos"
                )
            elif User[i]["revelacion"] == "aceptado":
                contraseña = User[i]["contraseña"]
                salt = sha256(contraseña.encode()).hexdigest()
                self.__Base[i] = {"salt":salt}
                Base[i] = {"salt":salt}
                actualizar()
                return f"Bienvenido {i}"
            else:
                return "desconocido"
    def iniciar_sesion(self, nombre:str, contraseña:str):
        if nombre.casefold() not in self.__Base:
            return Errores.get(
                "no-existe",
                "parece que estamos teniendo errores desconocidos"
            )
        salt = sha256(contraseña.encode()).hexdigest()
        if self.__Base[nombre.casefold()]["salt"] == salt:
            return f"Bienvenido {nombre.casefold()}"
class seguridad:
    def __init__(self, system):
        self._system = system
    def recibir_datos(self, User:dict):
        data = self._system.enviar_datos()
        for i in User:
            try:
                user1 = Usuari(nombre=i, Password=User[i]["contraseña"])
            except ValidationError as error:
                for e in error.errors():
                    errore = e["loc"][0]
                    Usuario1 = {i:{"revelacion":"rechazado", "causa":errore}}
                    return self._system.recibir_datos(Usuario1)
            else:
                if i in data:
                    Usuario = {i:{"revelacion":"rechazado", "causa":"repetido"}}
                    return self._system.recibir_datos(Usuario)
                Usuario2 = {i:{"revelacion":"aceptado", "contraseña":User[i]["contraseña"]}}
                return self._system.recibir_datos(Usuario2)
class registro:
    def __init__(self, seguridad):
        self.segurity = seguridad
    def registrarse(self, nombre:str, contraseña:str):
        Usuario = {nombre.casefold():{"contraseña":contraseña}}
        return self.segurity.recibir_datos(Usuario)
system = System()
segurity = seguridad(system)
registrarse = registro(segurity)
@app.get("/")
def entrada():
    return "ve a (registrarse)"
#probar
@app.post("/registrarse")
def registrar(Usuario:dict):
    for i in Usuario:
        nombre = i
        contraseña = Usuario[i]["contraseña"]
        mensaje = registrarse.registrarse(nombre, contraseña)
        return mensaje
@app.post("/iniciar-sesion")
def iniciar_sesion(Usuario:dict):
    for i in Usuario:
        nombre = i
        contraseña = Usuario[i]["contraseña"]
        mensaje = system.iniciar_sesion(nombre, contraseña)
        return mensaje