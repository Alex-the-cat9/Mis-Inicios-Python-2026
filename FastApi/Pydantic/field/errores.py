from pydantic import BaseModel, Field, ValidationError
class herramientas(BaseModel):
    IA:str
    contraseña:str = Field(min_length=4)
    codigo_de_5_digitos:str = Field(min_length=5, max_length=5)
diccionario_de_errores = {
    "contraseña":"la contraseña deve tener minimo 4 caracteres por seguridad",
    "codigo_de_5_digitos":"el codigo deve tener minimo 5 digitos"
}
if __name__ == "__main__":
    try:
        Computadora = herramientas(IA="openai", contraseña="petesto102", codigo_de_5_digitos="r216")
    except ValidationError as lista_de_error:
        for errores in lista_de_error.errors():
            campo = errores["loc"][0]
            print(diccionario_de_errores.get(
                campo,
                "el sistema no encontro el error"
            ))
