from typing import Final
from hashlib import sha256
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
class User(BaseModel):
    Nombre:str = Field(min_length=2)
    Contraseña:str = Field(min_length=4)

Diccionario_Errroes = {
    "Nombre":"El nombre deve ser un minimo de 2 caracteres",
    "Contraseña":"La contraseña deve de ser un minimo de 4 caracteres",
    "Repetido":"El nombre que quiso registrarse ya existe",
    "no-existe":"El nombre que puso no existe en la base de datos (ayuda:(pruebe con minusculas guardamos los nombres en minusculas))"
}
class System:
    def __init__(self):
        self.__Base = {}
    def dar_datos(self):
        return self.__Base
    def obtener(self, Usuario):
        for i in Usuario:
            if Usuario[i]["pendiente"] == "rechazado":
                return Diccionario_Errroes.get(
                    Usuario[i]["rechazado"],
                    "parece que nuestro servidor esta fallando un poco")
            else:
                Usuario1 = User(Nombre=i, Contraseña=Usuario[i]["contraseña"])
                salt = sha256(Usuario1.Contraseña.encode()).hexdigest()
                hora = datetime.now()
                self.__Base[i] = {"salt":salt, "hora":f"año:{hora:%Y} Mes:{hora:%m}  Dia:{hora:%d} hora:{hora:%H}:{hora:%M}"}
                return "Se registro correctamente"
    def iniciar_sesion(self, Usuario:str, contraseña:str):
        if Usuario not in self.__Base:
            return Diccionario_Errroes.get(
                "no-existe",
                "parece que nuestro servidor esta fallando un poco"
            )
        salt1 = sha256(contraseña.encode()).hexdigest()
        if self.__Base[Usuario]["salt"] == salt1:
            return f"Bienvenido {Usuario}"
class Registrar:
    def __init__(self, seguridad):
        self.enviar = seguridad
    def registrarse(self):
        nombre = input("Ponga su nombre: ").casefold()
        contraseña = input("ponga su contraseña: ")
        Usuario = {nombre:{"contraseña":contraseña}}
        return self.enviar.recibir(Usuario)
class Seguridad_registro:
    def __init__(self, system):
        self.Base = system
        self._Base_de_datos = self.Base.dar_datos()
    def recibir(self, Usuario:dict):
        completado = {}
        for i in Usuario:
            try:
                Usuario1 = User(Nombre=i, Contraseña=Usuario[i]["contraseña"])
            except ValidationError as error:
                for e in error.errors():
                    errores = e["loc"][0]
                    completado[i] = {"rechazado":errores, "pendiente":"rechazado"}
            else:
                if i in self._Base_de_datos:
                    completado[i] = {"rechazado":"Repetido", "pendiente":"rechazado"}
                else:
                    completado[Usuario1.Nombre] = {"pendiente":"aceptado", "contraseña":Usuario1.Contraseña}
        return self.Base.obtener(completado)
if __name__ == "__main__":
    syste = System()
    seguridad = Seguridad_registro(syste)        
    registro = Registrar(seguridad)
    usuario = registro.registrarse()
    while True:
        print("\n--- MENÚ ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            resultado = registro.registrarse()
            print(f"[SERVIDOR]: {resultado}")
        elif opcion == "2":
            user = input("\nUsuario: ").casefold()
            pas = input("Contraseña: ")
            print(f"[SERVIDOR]: {syste.iniciar_sesion(user, pas)}")
        elif opcion == "3":
            break