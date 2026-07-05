from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class datos(BaseModel):
         ip: int
         nombre: str
         empleo: str
         ganancia: int
@app.post("/datos-user")
def mostrar(usuario:datos):
        return {
         "mensaje_ip": f"tu ip es: {usuario.ip}",
         "nombre_recibido": usuario.nombre,
         "empleo_recibido": usuario.empleo,
         "ganancia_recibida": usuario.ganancia
         }