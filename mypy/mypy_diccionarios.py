#🏛️ EL PLANO DE INGENIERÍA:
#Todo en un solo archivo hangar.py
#Pica tus propios bloques de código en texto plano siguiendo estrictamente estas especificaciones de ciberdefensa 
#:1. El Plano de Hierro (La Estructura Fija)Ve al piso de arriba de tu archivo e importa la herramienta secreta: from typing import
#TypedDict
#Diseña el plano del diccionario llamado class TelemetriaNave(TypedDict): con exactamente estas 3 llaves fijas:
#modelo: Debe ser estrictamente un texto plano (str) .hiperviajes: Debe ser estrictamente un número entero (int) .nucleo_estable:
#Debe ser estrictamente un valor booleano (bool) .2.
#La Instanciación (El Diccionario Real)Crea un diccionario vivo aplicando tu estructura:
#nave_alex: TelemetriaNave = { ... } .La Trampa del Sabotaje (Tu Misión) 🧪:
#Vas a meterle un cable corrupto a propósito para poner a prueba tu radar láser . Modifica el valor de hiperviajes y en lugar de ponerle
#un número entero, inyéctale un texto plano (ejemplo: "veinte" o "muchos") .3.
#El Motor de Auditoría (Tu Función Pura)Crea una función llamada auditar_nave que reciba ese diccionario .La Aduana
# de Parámetro (Guardaespaldas): Obliga al parámetro a seguir el mismo tipo escribiendo datos:
#TelemetriaNave y promete que la salida será un texto plano (-> str) .La función solo debe retornar un f-string
#limpio formateando los datos de la nave .📡 Tu Bitácora de Reporte (Lo que debes hacer en tu máquina)
#Dale a Guardar en tu VS Code. Abre tu PowerShell de Windows y ejecuta el escáner de contrainteligencia de tipos:
#powershellmypy hangar.py
#Usa el código con precaución.Analiza las letras rojas que te escupió la consola y respóndeme con la ley marcial en la mano 
#:qué número de línea exacta te marcó mypy como corrupta y cuál es el mensaje físico en inglés que te arrojó para avisarte que
#el texto plano "veinte" destruyó el contrato del entero (int) [INDEX_3
from typing import TypedDict, List

class Persona(TypedDict):
    nombre: str
    edad: int

# ESTA es la base de datos real: una lista vacía que acumulará todo
lista_de_personas: List[Persona] = []

print("--- REGISTRO DE USUARIOS (Escribe 'salir' en el nombre para terminar) ---")

while True:
    nombre = input("\nDi tu nombre: ").strip().lower()
    
    if nombre == 'salir':
        break  # Rompe el bucle y deja de pedir datos
        
    try:
        edad = int(input("Di tu edad: "))
    except ValueError:
        print("Error: Edad inválida. Se asignará 15 por defecto.")
        edad = 15
        
    # Creamos el diccionario individual
    nueva_persona: Persona = {
        "nombre": nombre,
        "edad": edad
    }
    
    # ¡AQUÍ ES DONDE SE METE EL DATO DE VERDAD! Lo inyectamos a la lista
    lista_de_personas.append(nueva_persona)

# Al final, mostramos toda la colección acumulada
print("\n--- DATOS GUARDADOS EN MEMORIA ---")
print(lista_de_personas)