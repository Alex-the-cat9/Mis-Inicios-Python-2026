from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
class numero(BaseModel):
    operacion:str
    primer:int | float
    segundo:int | float
app = FastAPI(title="probando errores")
#vi que estos codigos son iguales al de python pueden tener el error de zerodivision error y tambien otros..
colapsos = 0
@app.get("/")
def bienvenida():
    return "entra a numerar '/numerar' para hacer tus calculos primero pon suma resta multiplicacion o division en ese orden luego dos numeor \
        en un formato json"
@app.post("/numerar", status_code=status.HTTP_201_CREATED)
def calculo(Base:numero):
    global colapsos
    if Base.operacion == "sumar":
        resultado = Base.primer + Base.segundo
        return f"el resultado es:{resultado}"
    elif Base.operacion == "restar":
        resultado = Base.primer - Base.segundo
        return f"el resultado es:{resultado}"
    elif Base.operacion == "multiplicacion":
        resultado = Base.primer * Base.segundo
        return f"el resultado es:{resultado}"
    elif Base.operacion == "division":
        try:
            resultado = Base.primer / Base.segundo
        except Exception as error_divisioncero:
            colapsos += 1
            print(f"alguien intento dividir en cero nuestro sistema funciono y detuvo la caida del servidor uvicorn colapsos evitados:{colapsos}")
            print(f"error:{error_divisioncero}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="intentaste dividir en cero"
            )
        else:
            return f"el resultado es:{resultado}"
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="error desconocido"
        )