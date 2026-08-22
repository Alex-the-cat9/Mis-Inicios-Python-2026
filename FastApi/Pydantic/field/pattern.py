from pydantic import BaseModel, Field, ValidationError
class Auto(BaseModel):
    Marca:str = Field(pattern=r"^[A-Z]+$")
    codigo:str = Field(min_length=4, max_length=4, pattern=r"^\d+$")
Diccionario_de_errores = {
    "Marca":"ERROR:solo se permite marcas con letras mayusculas de la A-Z",
    "codigo":"ERROR El codigo deve ser de exactamente 4 digitos de numeros del 0-9"
}
if __name__ == "__main__":
    try:
        Car1 = Auto(Marca="ALEX", codigo="4512")
    except ValidationError as error:
        for i in error.errors():
            Error = i["loc"][0]
            print(Diccionario_de_errores.get(
                Error,
                "El sistema no encontro el error"
            ))
    else:
        print(f"auto creado Marca:{Car1.Marca} codigo:{Car1.codigo}")
    #prueba
    try:
        Car2 = Auto(Marca="bugati", codigo="Alex")
    except ValidationError as error:
        for i in error.errors():
            Error = i["loc"][0]
            print(Diccionario_de_errores.get(
                Error,
                "El sistema no encontro el error"
            ))
    else:
        print(f"auto creado Marca:{Car2.Marca} codigo:{Car2.codigo}")
