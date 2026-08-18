from pydantic import BaseModel, Field
from requests import post, get
link = "http://127.0.0.1:8000"
print(get(f"{link}/"))
class Usuario_comun(BaseModel):
    name:str
    pasword:str = Field(min_length=4)
diccionario_traductor = {
    "<Response [200]>":"el servidor te acepto tu solicitud"
}
user1 = Usuario_comun(name="Alex", pasword="101alex")
registro = str(post(f"{link}/registrarse", json=user1.model_dump()))
print(diccionario_traductor.get(
    registro,
    "el servidor rechazo tu solicitud por un error"
))
print(registro)