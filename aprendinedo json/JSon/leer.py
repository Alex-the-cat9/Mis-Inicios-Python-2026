#Alex:este es la prueba de fuego leer.py
import json
with open("boveda.json", "r") as f:
    codigo = json.load(f)
print(codigo)