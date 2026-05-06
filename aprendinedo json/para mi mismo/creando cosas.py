import json
import sys
try:
    with open("privado.json", "r") as f:
        privacidad = json.load(f)
except FileNotFoundError:
    privacidad = {}
    with open("privado.json", "w", encoding="utf-8" ) as f:
        json.dump(privacidad, f, indent=4, ensure_ascii=False)
try:
    with open("recordatorio.json", "r") as f:
        pasado = json.load(f)
except FileNotFoundError:
    pasado = {}
    with open("recordatorio.json", "w", encoding="utf-8") as f:
        json.dump(pasado, f, indent=4, ensure_ascii=False)
def punto_de_guardado():
    with open("privado.json", "w", encoding="utf-8") as f:
        json.dump(privacidad, f, indent=4, ensure_ascii=False)
    with open("recordatorio.json", "w", encoding="utf-8")as f:
        json.dump(pasado, f, indent=4, ensure_ascii=False)
def agregar_privacidad(privacidad):
    que_descubriste = input("que descubriste hoy: ")
    nombre = input("nombre del responsable: ")
    privacidad[que_descubriste] = {"nombre":nombre}
    print("se guardo no se le olvidara")
    punto_de_guardado()
    return privacidad
def eliminar(privacidad):
    for e,i in privacidad.items():
        print(f"asunto:{e} nombre:{i["nombre"]}")
    elimina = input("a quien decea eliminar Alex: ")
    if elimina in privacidad:
        pasado[elimina] = privacidad[elimina]
        del privacidad[elimina]
        punto_de_guardado()
    else:
        print("Alex programame bien porfavor")
intentos = 3
while True:
    Contraseña = 2255
    try:
       if intentos <= 0:
           print("se te acabaron los intentos ahora espera 1000 años para volver a intentarlo")
           sys.exit()
           

       intento = int(input("dime la contraseña para acceder a este sitio: "))
    except ValueError:
        print("contraseña incorrecta quisas es porque intentaste escribir letras pista:la contraseña es de numeros")
        intentos -= 1
        continue
    if intento == Contraseña:
        print("bienvenido Alex")
        break
    else:
        print(f"contraseña incorrecta")
        intentos -= 1
while True:
    opciones = input("que decea hacer Alex [agregar] [eliminar] [salir] [ver]: ")
    if opciones == "agregar":
        privacidad = agregar_privacidad(privacidad)
    elif opciones == "eliminar":
        eliminar(privacidad)
    elif opciones == "salir":
        print("saliendo...")
        break
    elif opciones == "ver":
        preguntar = input("que decea ver su pasado oh sus problemas?: ")
        if preguntar == "problemas":
            for a,e in privacidad.items():
                print(f"problema:{a} nombre:{e}")
        elif preguntar == "pasado":
            for a,e in pasado.items():
                print(f"problema:{a} nombre:{e}")

    



