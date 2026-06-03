import json
import os

carpeta_actual = os.path.dirname(__file__)
ruta_perfecta = os.path.join(carpeta_actual, "Datos.json")

def conectar(diccionario_de_datos):
   with open(ruta_perfecta, "w", encoding="utf-8") as f:
      json.dump(diccionario_de_datos, f, indent=4)
class Conectar:
    def __init__(self, nombre, edad):
       self.nombre = nombre
       self.edad = edad
    def __str__(self):
       return f"nombre:{self.nombre} edad:{self.edad}"

        