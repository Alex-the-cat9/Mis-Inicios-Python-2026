#import json

#with open("base_de_datos_basado_ensure.json", "r", encoding="utf-8") as archivo:
#datos = json.load(archivo)
#print(datos)
#for llave,e in datos.items():
#    if "nombre" in datos:
#        print(f"{llave}:{e}")
#    if "edad" in datos:
#        print(f"{llave}:{e}")
#🏆 El Reto: "El Limpiador de Emojis"Tu objetivo: Tienes que crear un script que lea ese diccionario
#pero con tres condiciones específicas.Instrucciones:Detección: El programa debe detectar si el mensaje contiene
#el emoji de carita negra (☻).Modificación: Si lo contiene, debe crear una nueva clave llamada "status" con el valor
#"especial".Exportación Perfecta: Debes guardar el resultado en un archivo llamado resultado.json.
#El archivo debe ser legible para humanos,
#es decir:Los emojis deben verse como emojis (no \uXXXX).El archivo debe tener una sangría (indent) de 4 espacios.
import json
with open("base_de_datos_basado_ensure.json", "r", encoding="utf-8") as archivo:
    un_punto = json.load(archivo)
with open("base_de_datos_basado_ensure.json", "w", encoding="utf-8") as cargando:
    json.dump(un_punto, cargando, ensure_ascii=False, indent=4)
for e in un_punto:
    print(un_punto)
