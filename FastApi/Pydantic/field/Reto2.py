#El Reto: El Registro de Clientes VIP 💎Vas a programar el sistema de validación para una aplicación móvil de un banco.
#Debes crear un modelo en Pydantic llamado ClienteVIP con las siguientes reglas estrictas:nombre_usuario: Un texto (str)
#que debe medir mínimo 3 caracteres y máximo 12 caracteres.pin_seguridad: Un texto (str) que debe medir exactamente 4 caracteres.
#Además, mediante un pattern, debes obligar a que solo contenga números (r"^\d+$").saldo_inicial: Un número decimal o entero (float).
#El banco exige que para ser VIP el cliente deposite más de 1000 dólares (mayor estricto, usa tu regla de la letra t) y un máximo de 50000
#dólares (menor o igual, usa tu regla de la letra e).
from pydantic import BaseModel, Field, ValidationError
class ClienteVIP(BaseModel):
    nombre_usuario: str = Field(min_length=3, max_length=12)
    pin_seguridad: str = Field(min_length=4, max_length=4, pattern=r"^\d+$")
    saldo_inical: float = Field(gt=1000, le=50000)
Diccionario_de_errores = {
    "nombre_usuario":"el nombre de usuario deve ser un minimo de 3 a 12 letras",
    "pin_seguridad":"el pin de seguridad deve ser obligatoriamente 4 numeros del 0-9",
    "saldo_inicial":"para ser cliente VIP necesita depositar un minimo estricto de 1000USD y un maximo de 50000USD"
}
if __name__ == "__main__":
    try:
        Cliente1 = ClienteVIP(nombre_usuario="Alex", pin_seguridad="4391", saldo_inical=2500)
    except ValidationError as error:
        for i in error.errors():
            errores = i["loc"][0]
            print(Diccionario_de_errores.get(
                errores,
                "el sistema no encontro el error"
            ))
    else:
        print(f"Bienvenido clienteVIP {Cliente1.nombre_usuario}")
    try:
        Cliente2 = ClienteVIP(nombre_usuario="A", pin_seguridad="GG", saldo_inical=100)
    except ValidationError as error:
        for i in error.errors():
            errores = i["loc"][0]
            print(Diccionario_de_errores.get(
                errores,
                "el sistema no encontro el error"
            ))
    else:
        print(f"Bienvenido clienteVIP {Cliente2.nombre_usuario}")