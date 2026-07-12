#Alex:bien entonces desde la web el usuario pide cosas el internet publico va activa el api que no se que hace
#el api va a los servidores web que supongo que son json donde guarda cosas y luego va a la terminal que devulve lo que el usuario pidio
from fastapi import FastAPI # Aquí la "F" debe ser mayúscula

app = FastAPI()
@app.post("/sumas_matematicas")
def sumas(numero1:int,numero2:int, tipo:str):
    if tipo.lower() == "suma":
        return numero1 + numero2
    elif tipo.lower() == "resta":
        return numero1 - numero2
    elif tipo.lower() == "multiplicacion":
        return numero1 * numero2
#Alex:me cuesta mucho entender esto pero se que lo lograre por ahora dependo de /docs