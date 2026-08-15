from pydantic import Field, BaseModel, ValidationError

class Usuario(BaseModel):
    username: str = Field(min_length=2, max_length=10)
    password: str = Field(min_length=3)
DICCIONARIO_ERRORES = {
    "username": "El nombre de usuario debe tener entre 2 y 10 caracteres.",
    "password": "La contraseña es muy corta. Debe tener al menos 3 dígitos."
}
if __name__ == "__main__":
    try:
        usuario_invalido = Usuario(username="A", password="12")
    except ValidationError as e:
        print("🚨 REGISTRO RECHAZADO:")
        for error in e.errors():
            campo_fallido = error["loc"][0]
            mensaje = DICCIONARIO_ERRORES.get(
                campo_fallido,
                "el sistema no encontro un mensaje claro para su error"
            )
            print(mensaje)
#Alex:ya lo entiendo mucho mejor aprovecho para decir que la demora de sobre los archivos y solo estoy subiendo 1x1 es porque me cuesta mucho
#la escuela me quita mucho tiempo ademas me gusta ver que hace linea por linea y investigo escribo en mi libro memorizo y luego perfecciono me toma horas