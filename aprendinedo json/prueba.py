#dale un reto sin pistas
#Bien. Aquí tienes un reto de programación para Alex, sin pistas y sin ayuda.
#🧠 Reto: Sistema de Empresa Autónoma📌 Objetivo
#Crear un programa en Python que simule una empresa básica con control de empleados, dinero y seguridad.📋 Requisitos obligatorios
#El programa debe:
#1. 🏢 Empresa
#Tener una “empresa” con:
#dinero inicial
#lista de empleados
#2. 👤 Empleados
#Poder:
#contratar empleados
#despedir empleados
#ver lista de empleados
#3. 💰 Economía
#Cada empleado debe generar dinero automáticamente cuando se ejecuta una función de “ciclo de trabajo”
#El dinero de la empresa debe actualizarse
#4. 🔐 Seguridad
#Debe haber un sistema de acceso con contraseña
#Máximo 3 intentos
#Si falla, el sistema debe bloquear operaciones
#5. 📂 Persistencia
#Todo debe guardarse en un archivo (JSON o TXT)
#Al reiniciar el programa, los datos deben seguir ahí
#6. 🧠 Lógica obligatoria
#Debe usar clases (mínimo 2)
#Debe usar funciones dentro de clases
#Debe usar try/except
#Debe usar bucles de menú (while True)

#🚫 Restricciones
#No usar librerías externas
#No copiar código de internet
#No usar código ya hecho que solo modifique datos manualmente
#🏁 Condición de victoria
#El programa debe poder:
#iniciar
#crear empleados
#generar dinero
#guardar datos
#y volver a cargarlos sin perder nada
import json
import time
try:
    with open("empresa.json", "r")as f:
        empresa = json.load(f)
except FileNotFoundError:
    empresa = {
    "dinero":9910, 
    "empleados":{}}
    with open("empresa.json", "w", encoding="utf-8") as f:
        json.dump(empresa, f, indent=4, ensure_ascii=False)
def punto_de_guardado():
    with open("empresa.json", "w", encoding="utf-8") as f:
        json.dump(empresa, f, indent=4, ensure_ascii=False)
class vereficacion:
    def __init__(self, nombre, trabajo):
        self.nombre = nombre
        if nombre in empresa["empleados"]:
            raise NameError("empleado ya existe")
        self.trabajo = trabajo
        empresa["empleados"][nombre] = trabajo
        empresa["dinero"] += 300
        punto_de_guardado()
def despedir():
    despido = input("que empleado decea despedir?: ").lower()
    if despido in empresa["empleados"]:
        print("despidiendo...")
        del empresa["empleados"][despido]
        punto_de_guardado()
    else:
        print("incorrecto")
class registro(vereficacion):
    empleos = ["desarrollador", "ingeniero", "limpieza", "web"]
    def __init__(self):
        usuario = input("dime su nombre: ")
        if len(usuario) < 3:
            raise NameError("nombre no existe")
        if "1" in usuario or "2" in usuario or "3" in usuario or "4" in usuario or "5" in usuario or "6" in usuario or "7" in usuario or "8" in usuario or "9" in usuario or "0" in usuario:
            raise NameError("nombre con numeros")
        empleo = input(f"mm vale {usuario} que empleo quiere usted en nuestra empresa [desarrollador] [ingeniero] [limpieza] [web]: ").lower()
        if empleo in self.empleos:
            print(f"vale ya te contratamos empiezas mañana de {empleo}")
            super().__init__(usuario, empleo)
        else:
            print("me parece que ese empleo no esta en la lista")
            raise ValueError("no empleado en la lista")
def seguridad():
    CONTRASEÑA = 9011
    intentos = 3
    while intentos > 0:
        try:
            intento = int(input("ingrese su contraseña: "))
        except ValueError:
            intentos -=1
            print(f"incorrecto te quedan {intentos}")
            continue
        if intento == CONTRASEÑA:
            print("bienvenido")
            break
        else:
            intentos -= 1
            print(f"contraseña incorrecta te quedan {intentos}")
    if intentos > 0:
        return True
    else:
        return False
while True:
    user = input("que decea [registrarse] [base de datos] [salir] [despedir]: ").lower()
    if user == "salir":
        print("gracias")
        break
    elif user == "despedir":
        despedido = despedir()
    elif user == "base de datos":
        acceso = seguridad()
        if acceso:
            try:
               for nombre,contenido in empresa.items():
                 print(F"{nombre}:{contenido}")
            except KeyError:
                print("no se ah puesto nada por ahora")
        else:
            print("para volver a la sala necesita esperar tiempo...")
            time.sleep(900)
    elif user == "registrarse":
        try:
          empleado = registro()
        except ValueError:
            print("parece que no esta en la lista")
            continue
        except NameError:
            print("error al colocar nombre")
            continue
    else:
        print("opcion no existe")
            
  
        
