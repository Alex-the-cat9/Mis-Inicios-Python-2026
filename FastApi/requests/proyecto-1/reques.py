from fastapi import FastAPI
from pydantic import BaseModel
from secrets import token_hex
import json
from typing import Any
seguridad = str(token_hex(32))
app = FastAPI(docs_url=f"/{seguridad}")
with open("token_docs.txt", "w", encoding="utf-8") as f:
    f.write(f"token es:{seguridad}")
clientes: dict[Any, Any] = {"registrados":[]}
try:
    with open("usuarios.json", "r") as user:
        clientes = json.load(user)
except FileNotFoundError:
    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)
def cargar_progreso():
    with open("usuarios.json", "w", encoding="utf-8") as f:
        json.dump(clientes, f, indent=4, ensure_ascii=False)
class registrarse(BaseModel):
    nombre:str
    edad:int
@app.options("/ver-estado")
def ver_opciones():
    return "usuario puede entrar a nuestro post |/registro| para registrar su nombre y edad texto y un numero entero" \
    "tambien puede ir a |/cambiar-nombre| donde deve enviar su nombre y su nuevo nombre tambien puede ir a |ver-nombre| donde" \
    "podra ver su nombre y su edad, sirve para ver si el sistema te registro puede ir a nuestro |/eliminar| donde le eliminamos" \
    " su nombre edad, y una ultima cosa no trate de ir a docs es casi imposible"
@app.get("/ver-nombre")
def ver(nombre:str):
    for i in clientes["registrados"]:
        if nombre in i:
            return f"su nombre:{nombre} su edad:{i[nombre]}"
    return "no se encontro el nombre"
@app.post("/registro")
def guardar(molde:registrarse):
    if molde.edad <= 0:
        return "numeros negativos"
    elif len(molde.nombre) <=2:
        return "nombre corto casi imposible de creer"
    for i in clientes["registrados"]:
        if molde.nombre in i:
            return "nombre ya existe"
    clientes["registrados"].append({molde.nombre:molde.edad})
    cargar_progreso()
    return "ya se registro"
@app.put("/cambiar-nombre")
def cambiar(nombre:str, nuevo_nombre:str):
    for i in clientes["registrados"]:
        if nombre in i:
            i[nuevo_nombre] = i.pop(nombre)
            cargar_progreso()
            return f"se cambio su nombre a:{nuevo_nombre}"
    return f"el nombre:{nombre} no esta en la lista"
@app.delete("/eliminar")
def eliminacion(nombre:str):
    for i in clientes["registrados"]:
        if nombre in i:
            clientes["registrados"].remove(i)
            cargar_progreso
            return "ya fue eliminado"
    return "no se encontro su nombre"


    
    