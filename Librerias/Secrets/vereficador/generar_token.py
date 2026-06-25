from IA_vereficador_de_seguridad import IA_vereficador_de_seguridad
from secrets import token_bytes, token_hex
def generar_token(seguridad:str) -> str:
    if seguridad == "maxima":
        return str(token_bytes(30))
    elif seguridad == "media":
        return token_hex(30)
    elif seguridad == "baja":
        while True:
            try:
                token = input("pon tu contraseña [deve superar los 10 caracteres]: ").strip()
                IA_vereficador_de_seguridad(token)
            except PermissionError as error:
                print(str(error))
            else:break
    return token