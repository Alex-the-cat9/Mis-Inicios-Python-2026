from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
app = FastAPI()
class Usuario(BaseModel):
    nombre: str
    contraseña: str = Field(min_length=3)
    trabajo: str = Field(default="cliente")
    codigo_de_4digitos: str = Field(pattern=r"^\d{4}$")
    registrado_el: datetime = Field(default_factory=datetime.now)
DICCIONARIO_ERRORES = {
    "contraseña": "la contraseña debe ser un mínimo de 3 dígitos",
    "codigo_de_4digitos": "el código debe ser exactamente de 4 dígitos"
}
base_de_datos = {}
@app.post("/registrar")
def registrar_usuario(usuario_entrante: Usuario):
    if usuario_entrante.nombre in base_de_datos:
        raise HTTPException(status_code=400, detail="Este nombre de usuario ya está registrado.")
    base_de_datos[usuario_entrante.nombre] = usuario_entrante
    return {
        "mensaje": f"Bienvenido {usuario_entrante.nombre}",
        "trabajo_asignado": usuario_entrante.trabajo,
        "registrado_a_las": usuario_entrante.registrado_el
    }
