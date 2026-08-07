from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from pydantic import BaseModel
from typing import Final
from secrets import token_hex
import os
ruta_carpeta = os.path.abspath("templates")#crea la ruta exacta de la carpeta templates
Secret_token: Final[str] = token_hex(15)#
app = FastAPI(title="primer_backend", docs_url=f"/{Secret_token}", redoc_url=f"/{Secret_token}")#
templates = Jinja2Templates(directory=ruta_carpeta)#le da media logica de python y le pone oidos a todos los archivos html que se encuentren dentro de esa carpeta
class registro(BaseModel):#
    Nombre:str#
    edad:int#
@app.get("/", response_class=HTMLResponse)#preparate vamos ir a un archivo html
def mostrar(request:Request):return templates.TemplateResponse(request=request, name="practica.html", context={"dat":{"Nombre":"Alex", "edad":10}})
@app.post("/crear-item", response_class=HTMLResponse)
def procesar_formulario(
    request: Request, 
    Nombre: str = Form(...),
    edad: int = Form(...)
):
    Datos_validos = registro(Nombre=Nombre, edad=edad)
    return templates.TemplateResponse(
        request=request, 
        name="practica.html",                                                   
        context={"dat":Datos_validos}
    )