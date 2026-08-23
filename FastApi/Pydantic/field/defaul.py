from pydantic import BaseModel, Field, ValidationError
class Usuario(BaseModel):
    nombre: str
    contraseña: str = Field(min_length=3)
    trabajo: str = Field(default="cliente")
    codigo_de_4digitos: str = Field(pattern=r"^\d{4}")
Diccionario_de_errores = {
    "contraseña":"la contraseña deve ser un minimo de 3 digitos",
    "codigo_de_4digitos":"el codigo deve ser exactamente 4 digitos"
}
if __name__ == "__main__":
    try:
        user1 = Usuario(nombre="Alex", contraseña="alexito103", trabajo="desempleado", codigo_de_4digitos="1012")
    except ValidationError as error:
        for i in error.errors():
            errore = i["loc"][0]
            print(Diccionario_de_errores.get(
                errore,
                "el error no a sido encontrado pero ya mandamos una nota al programador"
            ))
    else:
        print(f"bienvenido {user1.nombre} su trabajo:{user1.trabajo}")
    try:
        user2 = Usuario(nombre="Ale", contraseña="pepe1031", codigo_de_4digitos="1110")
    except ValidationError as error:
        for i in error.errors():
            errore = i["loc"][0]
            print(Diccionario_de_errores.get(
                errore,
                "el error no a sido encontrado pero ya mandamos una nota al programador"
            ))
    else:
        print(f"bienvenido {user2.nombre} su trabajo:{user2.trabajo}")
    