from requests import get, post
from pydantic import Field, BaseModel
server = "http://127.0.0.1:8000"
class user(BaseModel):
    nombre:str
    contraseña: str = Field(min_length=5)
datos = user(nombre="Alex", contraseña="891021")
respuesta = get(server).text
print(respuesta)
registro = post(f"{server}/registro", json=datos.model_dump())
print(registro.text)
#version prime
prime = post(f"{server}/prime", params={"nombre": "Alex"})
print(prime.text)
#puede soportar varios user
datos1 = user(nombre="alexander", contraseña="22211112")
datos2 = user(nombre="mark", contraseña="192990")
datos3 = user(nombre="martes", contraseña="019212")
datos4 = user(nombre="nacho", contraseña="32013")
registro1 = post(f"{server}/registro", json=datos1.model_dump())
registro2 = post(f"{server}/registro", json=datos2.model_dump())
registro3 = post(f"{server}/registro", json=datos3.model_dump())
registro4 = post(f"{server}/registro", json=datos4.model_dump())
print(f"se registro alexander:{registro1.text}")
print(f"se registro mark:{registro2.text}")
print(f"se registro martes:{registro3.text}")
print(f"se registro nacho:{registro4.text}")
#SEGURIDAD
registro_intento = post(f"{server}/registro", json=datos.model_dump())
print(f"no dejo pasar nombres repetidos:{registro_intento.text}")
#prime no repetidos
prime = post(f"{server}/prime", params={"nombre": "Alex"})
print(f"alex ya tenia la version prime:{prime.text}")
