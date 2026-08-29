from fastapi import FastAPI
from pydantic import BaseModel, Field
from datetime import datetime
app = FastAPI()
class Usuario(BaseModel):
    nombre: str
    trabajo: str = Field(default="cliente")
    registrado_el: datetime = Field(default_factory=datetime.now)
@app.post("/crear-usuario")
def crear(user: Usuario):
    return {
        "mensaje": f"¡Usuario {user.nombre} creado con éxito!",
        "trabajo": user.trabajo,
        "hora_de_tu_pc": user.registrado_el
    }
