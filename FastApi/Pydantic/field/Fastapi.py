from pydantic import Field, BaseModel
from random import SystemRandom
from fastapi import FastAPI
from typing import Final
#un reto divertido creado por mi
app = FastAPI()
seguridad = SystemRandom()
class Usuario_comun(BaseModel):
    name:str
    pasword:str = Field(min_length=4)
@app.get("/")
def bienvenida():
    return "USER entro a la pagina web"
@app.post("/registrarse")
def datos(User:Usuario_comun):
    return f"User:{User.name} Entro al server su cuenta a sido creada"