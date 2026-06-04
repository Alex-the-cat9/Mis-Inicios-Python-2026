from conectar2 import mis_Datos
from conectar1 import Conectar
import json
import os
carpeta_actual = os.path.dirname(__file__)
ruta_perfecta = os.path.join(carpeta_actual, "Datos.json")#ayuda de maestro en esta linea
def punto_de_guarado():
    with open(ruta_perfecta, "w", encoding="utf-8") as f:
        json.dump(mis_Datos, f, indent=4, ensure_ascii=False)
while True:
    user = input("[ver] [salir]  [agregar]: ").lower()
    if user == "salir":
        break
    elif user == "agregar":
        try:
            nombre = input("di el nombre: ")
            edad = int(input("di la edad: "))
        except ValueError:
            print("error:dijiste letras en la edad")
            continue
        else:
            nuevo = Conectar(nombre, edad)
            mis_Datos[nuevo.nombre] = edad
            punto_de_guarado()
    elif user == "ver":
        if len(mis_Datos) <= 0:
            print("error:no tienes Datos")
        else:
            print(mis_Datos)
    
    
        