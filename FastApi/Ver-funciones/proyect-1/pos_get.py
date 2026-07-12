import json
from fastapi import FastAPI
from typing import Any
#py -m uvicorn fastApi.pos_get:app --reload
app = FastAPI()
base_de_datos: dict[str, str | list | dict | Any ] = {
    "finanzas":"700",
    "Usuarios":{"Registrados":[]}
}
try:
    with open("Base_de_datos.json", "r", encoding="utf-8") as f:
        base_de_datos = json.load(f)
except FileNotFoundError:
    base_de_datos = {"finanzas":"700", "Usuarios":{"Registrados":[]}}
@app.post("/meter_datos")
def Datos(Usuario:str, contraseña:str):
    base_de_datos["Usuarios"]["Registrados"].append({Usuario:contraseña})
    with open("Base_de_datos.json", "w", encoding="utf-8") as f:
        json.dump(base_de_datos, f, ensure_ascii=False, indent=4)
    return "guardado con exito"
@app.get("/sacar_datos")
def Dato(Usuario:str):
    try:
        with open("Base_de_datos.json", "r") as f:
            codigo = json.load(f)
        for i in codigo["Usuarios"]["Registrados"]:
            for e in i:
                if e == Usuario:
                    return f"nombre:{e} contraseña:{i[e]}" 
    except Exception:
        return "error interactua primero con post"     
