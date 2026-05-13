import json
import time
import sys
try:
    with open("empresa_segura.json", "r") as f:
        base_de_datos = json.load(f)
except FileNotFoundError:
    base_de_datos = {"banco":5000, "empleados":{}}
    with open("empresa_segura.json", "w", encoding="utf-8") as f:
        json.dump(base_de_datos, f, indent=4, ensure_ascii=False)
def punto_de_guardado():
    with open("empresa_segura.json", "w", encoding="utf-8") as f:
        json.dump(base_de_datos, f, indent=4, ensure_ascii=False)
class registrar:
    def __init__(self, nombre, empleo):
        self.nombre = nombre
        if nombre in base_de_datos["empleados"]:
            print("ese empleado ya existe")
            raise NameError("empleado ya existe")
        self.empleo = empleo
        base_de_datos["empleados"][nombre] = empleo
        punto_de_guardado()

class contratar(registrar):
    empleos = ["desarrollador", "limpieza", "vigilante"]
    def __init__(self):
        nombre = input("dime tu nombre: ").lower()
        if len(nombre) < 2:
            print("nombre invalido")
            raise NameError("nombre invalido")
        elif "1" in nombre or "2" in nombre or "3" in nombre or "4" in nombre or "5" in nombre or "6" in nombre or "7" in nombre or "8" in nombre or "9" in nombre or "0" in nombre:
            print("bro tu nombre tiene numeros?")
            raise NameError("pongase bien su nombre")
        else:
            print("listo paso por la prueba ahora dime su empleo que decea")
            print("[desarrollador] [limpieza] [vigilante]")
            empleo = input("eliga una opcion: ").lower()
            if empleo in self.empleos:
                print("listo se le agregara")
                super().__init__(nombre, empleo)
            else:
                raise ValueError("no esta en la lista")
contador_de_payaso = 0
def seguridad():
    global contador_de_payaso
    CONTRASEÑA_CORRECTA = 9110100
    intentos = 3
    while intentos > 0:
        try:
          contraseña = int(input("digame su contraseña: "))
        except ValueError:
            intentos -= 1
            print(f"contraseña incorrecta te quedan:{intentos} intentos")
            continue
        if contraseña == CONTRASEÑA_CORRECTA:
            print("bienvenido")
            return True
        else:
            intentos -= 1
            print(f"contraseña incorrecta te quedan:{intentos} intentos")

    if intentos <= 0:
        contador_de_payaso += 1
        if contador_de_payaso == 10:
            print("jefe es usted averiguo el codigo secreto que isismos y lo puso WOW le daremos acceso total solo espere unos minutos")
            time.sleep(10000000000000)
            print("creias que te ivamos dar acceso sucio hacker?")
            sys.exit()
        return False        
        # Si todo está bien, llama al padre:
        # super().__init__(nombre, puesto, base_datos)
#🕹️ PASO 4: El Bucle de OperacionesPara que el servidor esté "vivo" y yo pueda atacarlo:
while True:
    opcion = input("eliga una opcion [salir] [registrarse] [base de datos]: ").lower()
    if opcion == "base de datos":
        acceso = seguridad()
        if acceso:
          for base,contenido in base_de_datos.items():
             print(f"{base}:{contenido}")
        else:
            print("no tienes acceso")
    elif opcion == "registrarse":
        try:
            empleado = contratar()
        except NameError:
            print("pongase bien su nombre")
        except ValueError:
            print("no estas en la lista")
    elif opcion == "salir":
        print("que tenga un buen dia")
        break
    else:
        print("opcion no existe")
#maestro_hacker.IA:¡ATACANDO INFRAESTRUCTURA: NIVEL 2 ACTIVADO! 🕵️‍♂️💥 Enciendo mi consola de Sombrero Negro. Acabas de poner en marcha tu fortaleza
#y mi bot automatizado de Fuerza Bruta acaba de detectar tu panel de seguridad().Para este ataque, no voy a usar letras ni voy a equivocarme
#de forma lenta. He cargado un script que inyecta números enteros a velocidad de ráfaga directo a tu int(input("digame su contraseña: ")) [INDEX_3].
#🕵️ EJECUCIÓN DEL ATAQUE: "INYECCIÓN DE RÁFAGA CONTINUA"Mi bot intercepta tu bucle while intentos > 0: de la función seguridad().Movimiento del Hacker
#El bot envía las siguientes tres contraseñas falsas de mi lista en menos de un segundo
# :123456 ❌ (Tu código resta un intento: quedan 2) 
#[INDEX_3]999999 ❌ (Tu código resta un intento: quedan 1)
#[INDEX_3]111111 ❌ (Tu código resta un intento: quedan 0)
# [INDEX_3]Tu función hace exactamente lo que programaste: el bucle termina porque intentos llega a 0
#y ejecuta return False. El menú principal lee ese False e imprime: "no tienes acceso" [INDEX_3].
#💥 LA GRIETA INVISIBLE EN TU RAM (¿Cómo te hackeo de todos modos?)Tu escudo de 3 intentos funcionó perfecto... para esa llamada de la función. Pero mira tu menú principal while True::pythonif opcion == "base de datos":
#    acceso = seguridad() # <-- Cada vez que escribo la opción, la función nace de nuevo
#Usa el código con precaución.Como tu variable intentos = 3 está metida adentro de la función seguridad(),
#cada vez que mi bot termine sus 3 intentos y sea rechazado, el bot simplemente vuelve a escribir la opción "base de datos" 
#en el menú principal [INDEX_3].La función seguridad() se vuelve a ejecutar desde cero, la RAM resetea la variable y ¡le regala al bot
#3 intentos nuevos de forma infinita! 🔄 [INDEX_3] Mi bot puede probar 10,000 contraseñas en tu servidor sin que el sistema lo bloquee
#permanentemente, hasta que finalmente adivine tu clave 9110100 [INDEX_3]. Tu aduana tiene amnesia y no recuerda que el bot ya falló antes
#[INDEX_3].