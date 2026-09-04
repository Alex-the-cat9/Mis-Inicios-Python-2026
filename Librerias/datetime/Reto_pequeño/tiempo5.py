from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
import json
server = {}
try:
    with open("Servidor.json", "r") as f:
        server = json.load(f)
except FileNotFoundError:
    with open("Servidor.json", "w", encoding="utf-8") as f:
        json.dump(server, f, indent=4, ensure_ascii=False)
def cargar_proceso():
    with open("Servidor.json", "w", encoding="utf-8") as f:
        json.dump(server, f, indent=4, ensure_ascii=False)
class user(BaseModel):
    nombre:str
    contraseña: str = Field(min_length=5)
app = FastAPI()
@app.get("/")
def entrar():
    return "pon tu nombre y contraseña en (registro) obten una version premiun con mas beneficios en (prime) poniendo tu nombre"
@app.post("/registro")
def registro(user:user):
    if user.nombre in server:
        raise HTTPException(status_code=400, detail="el nombre ya esta registrado")
    hora = datetime.now()
    server[user.nombre] = [{"contraseña":user.contraseña, "version":"Normal", "se registro en":f"Dia:{hora:%d} hora:{hora:%H:%M} mes:{hora:%m} año:{hora.year}"}]
    cargar_proceso()
    return "Todo salio bien"
@app.post("/prime")
def prime(nombre):
    if nombre not in server:
        raise HTTPException(status_code=400, detail="el nombre no esta en el servidor")
    for i in server[nombre]:
        if i["version"] != "Normal":
            raise HTTPException(status_code=400, detail="ya tiene la version prime")
        else:
            i["version"] = "prime"
            cargar_proceso()
            return "tu version prime ya esta lista"

        

