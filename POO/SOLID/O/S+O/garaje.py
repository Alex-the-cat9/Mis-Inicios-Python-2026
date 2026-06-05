#📁 Archivo 2: garaje.py (El Motor de Datos y JSON - AISLADO)
#Su nombre dice: Controlar los casilleros de almacenamiento .Tu misión:
#Aquí creas tu diccionario central Flota = {} . Escribe dos funciones:cargar_datos():
#Usa tu ruta dinámica (os.path.join) para abrir flota.json en modo lectura ("r"),
#y succiona el contenido para rellenar tu diccionario .guardar_datos():
#Abre flota.json en modo escritura ("w") y estampa el diccionario limpio en el disco duro .
import json
import os#linea con ayuda
carpeta_actual = os.path.dirname(__file__)#linea con ayuda
ruta_perfecta = os.path.join(carpeta_actual, "flota.json")#linea con ayuda
flota = {"ultima_recorrida":{}}

def cargar_datos():
    global flota
    if os.path.exists(ruta_perfecta):
            with open(ruta_perfecta, "r") as f:
                flota = json.load(f)
def guardar_datos():
         global flota
         with open(ruta_perfecta, "w", encoding="utf-8") as f:
              json.dump(flota, f, indent=4, ensure_ascii=False)



