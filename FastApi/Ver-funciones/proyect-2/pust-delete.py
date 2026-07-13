#🛡️ OPERACIÓN: "EL PANEL DE CONTROL DE LA BÓVEDA OMEGA"
#El Escenario:Tu imperio está creciendo. Tienes una Bóveda donde registras a tus "Soldados" y detectas "Intrusos".
#Necesitas un sistema que te permita evolucionar a tus aliados y purgar a los traidores sin tener que borrar todo
#el archivo manualmente [Turn 42].
#Tu Misión Técnica (El Código):
#Estructura Inicial: Tu archivo Base_de_datos.json debe empezar con este molde (usando el try/except de carga inicial
#que ya perfeccionaste) [Turn 40]:
#RETO PUT (La Evolución):
#Crea el endpoint @app.put("/ascender_soldado").
#Lógica: Debe recibir el nombre del soldado y su nuevo_rango.
#Acción: Busca al soldado en la lista "Entidades". Si lo encuentras, actualiza su rango y súmale +50 a su poder [231, Turn 42].
#Tatuaje: Guarda el cambio usando las 3 Reglas del Tatuaje (indent=4, ensure_ascii=False, encoding="utf-8") [44, Turn 39].
#RETO DELETE (La Purga Forense):
#Crea el endpoint @app.delete("/eliminar_intruso").
#Lógica: Debe recibir el nombre de la entidad a eliminar.
#Acción: Realiza una purga quirúrgica. Busca el nombre en la lista y, si existe, extráelo usando .pop() o del [155, 167, Turn 42].
#Seguridad: Si el nombre es "Alex", el sistema debe lanzar un raise o un mensaje de "ERROR: No puedes eliminar al Creador" [Turn 42].
#Blindaje de Privacidad:
#En el encabezado de tu código, debe aparecer tu comando de mando universal para GitHub:
#py -m uvicorn fastApi.nombre:app --reload, para que nadie vea tus rutas privadas de chamb [Turn 38].
import json
from fastapi import FastAPI
try:
    with open("Base_de_datos_soldaderia.json", "r") as f:
        Base = json.load(f)
except FileNotFoundError:
    Base = {"Soldaderia":[]}
    with open("Base_de_datos_soldaderia.json", "w", encoding="utf-8") as f:
        json.dump(Base, f, indent=4, ensure_ascii=False)
def cargar_progreso():
    with open("Base_de_datos_soldaderia.json", "w", encoding="utf-8") as f:
        json.dump(Base, f, indent=4, ensure_ascii=False)

app = FastAPI()
@app.post("/contratar_soldado")
def contrato(nombre:str) -> str:
    Base["Soldaderia"].append({nombre:"Soldado-bajo"})
    cargar_progreso()
    return f"soldado {nombre} contratado su rango es:{"soldado bajo"}"
@app.put("/ascender_soldado")
def soldado(nombre:str, nuevo_rango:str):
    if nombre.lower() == "alex":
        return "no puedes cambiar el rango del general"
    for i in Base["Soldaderia"]:
        if nombre in i:
            cargar_progreso()
            return f"rango acendido señor {nombre} su nuevo rango es:{nuevo_rango}"
        else:
            return "soldado no existe"
@app.delete("/eliminar_intruso")
def eliminar(nombre:str):
    if len(Base["Soldaderia"]) <= 0:
        return "no ay soldados para eliminar"
    if nombre.lower() == "alex":
        return "no puedes eliminar al general"
    for i in Base["Soldaderia"]:
        for e in i:
            if e == nombre:
                Base["Soldaderia"].remove(i)
                cargar_progreso()
                return "eliminado"