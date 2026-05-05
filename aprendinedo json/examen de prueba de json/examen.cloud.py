#Demuéstrame JSON primero, que es lo más importante ahora.

#Ejercicio
#Crea un archivo Python que haga esto:
#1. Tienes esta información:
#Nombre: Tu nombre
#Edad: Tu edad  
#Lenguajes: Una lista con los que conoces
#2. Guárdala en un archivo datos.json
#3. Vuelve a leer ese archivo y muestra en pantalla:
#Nombre: Alex
#Edad: 15
#Lenguajes: Python

#Reglas:

#Sin buscar en Google
#Sin ver notas
#Solo tú y tu cabeza
import json
try:
    with open("datos.json", "r") as f:
        datos = json.load(f)
except FileNotFoundError:
    datos = {
        "nombre":"Alex",
        "edad":15,
        "lenguajes":["python"]
    }
    with open("datos.json", "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print(datos)