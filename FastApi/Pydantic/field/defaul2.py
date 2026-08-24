from pydantic import BaseModel, Field, ValidationError
from datetime import datetime 
class Usuario(BaseModel):
    nombre: str
    contraseña: str = Field(min_length=3)
    trabajo: str = Field(default="cliente")
    codigo_de_4digitos: str = Field(pattern=r"^\d{4}$")
    registrado_el: datetime = Field(default_factory=datetime.now)
diccionario_de_errores = {
    "contraseña": "la contraseña debe ser un mínimo de 3 dígitos",
    "codigo_de_4digitos": "el código debe ser exactamente de 4 dígitos"
}
if __name__ == "__main__":
    try:
        user1 = Usuario(nombre="Alex", contraseña="alexito103", trabajo="desempleado", codigo_de_4digitos="1012")
    except ValidationError as error:
        for i in error.errors():
            errore = i["loc"][0]
            print(diccionario_de_errores.get(errore, "el error no ha sido encontrado..."))
    else:
        print(f"Bienvenido {user1.nombre} | Trabajo: {user1.trabajo}")
        print(f"🕒 Registrado a la hora de tu PC: {user1.registrado_el}\n")
    try:
        user2 = Usuario(nombre="Ale", contraseña="pepe1031", codigo_de_4digitos="1110")
    except ValidationError as error:
        for i in error.errors():
            errore = i["loc"][0]
            print(diccionario_de_errores.get(errore, "el error no ha sido encontrado..."))
    else:
        print(f"Bienvenido {user2.nombre} | Trabajo: {user2.trabajo}")
        print(f"🕒 Registrado a la hora de tu PC: {user2.registrado_el}")
