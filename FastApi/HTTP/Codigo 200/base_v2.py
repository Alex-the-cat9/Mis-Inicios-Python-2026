#Alex:mm Hi, i´m Alex and not i´m bilingual xd
#bueno me intereso bastante sobre los codigos de estado http y sus errores ay respuestas de informacion respuestas de exito redicciones errores
#del cliente asta errores del servidor que viene por rangos
#Range 100:respuestas informativas
#Range 200:respuestas de exito
#Range 300:redirecciones
#Range 400:errores del cliente
#Range 500:errores del servidor
#voy aprender todos cada uno de ellos
from fastapi import FastAPI, status
from pydantic import BaseModel
app = FastAPI(title="codigos 100 y 200")
class pedir(BaseModel):
    accion:str
@app.get("/normal")
def mensaje():
    return {
        "esta es una accion normal 200 OK":"accion normal"
    }
@app.get("/")
def bienvenidad():
    return "bienvenido a los codigo 100 y 200"
@app.post("/crear-user_v2", status_code=status.HTTP_201_CREATED)
def otro(modo:pedir):
    return{
        f"Recibido":{modo.accion},
        "tipo de accion":"201 CREATED"
    }