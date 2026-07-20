#maestro.IA:async def 🚀: Le grita al servidor web: "¡Activa el modo malabarista para esta función! Esta zona del código tiene permiso
#para procesar múltiples tareas en paralelo en la PowerShell".await ⏳: Es el cable de seguridad. Se coloca únicamente antes
#de las tareas que sabemos que van a demorar (como leer tu archivo flota.json del disco duro o descargar un exploit de la red)
#Le dice a la CPU: "Pon a correr esta descarga, suelta el hilo de ejecución aquí y vete a atender otras peticiones de la interfaz
#mientras esto termina" [INDEX_3].
#Alex:es como cuando descargo algo en googlel descargo dos cosas y en vez de que se pause una se descarga las dos al mismo tiempo
#y algo mas creo que el await es como un tunel que le dice ven aqui por 3 segundos o por tanto tiwempo
# 🚀 Activamos el modo malabarista (descargar varias cosas a la vez)
import asyncio
from fastapi import FastAPI
app = FastAPI()
@app.get("/escaneo")
async def verificarIP():
    print("iniciando escaneo de IP sospechosa")
    await asyncio.sleep(4)
    print("resultado terminado")
    return {"resultado":"exitoso", "tiempo":"4 segundos", "IP":"IP limpia"}