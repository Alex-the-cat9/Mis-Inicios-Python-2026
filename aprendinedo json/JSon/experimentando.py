#🛡️ EL RETO: "LA BÓVEDA DEL CREADOR"Escenario:Eres el Arquitecto de un sistema de seguridad.
#  Tienes que crear un programa que guarde las "Llaves de Acceso" de tus amigos en un archivo llamado
#  boveda.json.Misión:Crea un diccionario vacío llamado llaves.Pide por input el nombre de un amigo y su código secreto
#  (un número).Guarda esos datos en el diccionario.El Tatuaje: Usa json.dump para guardarlo en el archivo boveda.json
#  con indent=4.La Prueba de Fuego: Cierra el VS Code, vuelve a abrirlo y crea otro script que use json.load para imprimir
#  en pantalla el código secreto de tu amigo.💻 Tu esquema de batalla (Completa los huecos):pythonimport json
import json
# 1. El Diccionario
boveda = {}

# 2. Los Inputs (Pregúntale al usuario)
nombre = input("👤 Nombre del agente: ")
codigo = int(input("🔑 Código de acceso: "))

# 3. Meterlo al diccionario
boveda[nombre] = codigo

# 4. GUARDAR (Usa el "w" para crear el archivo)
with open("boveda.json", "w") as f:
    json.dump(boveda, f, indent=4)

print("✅ Llave guardada en la bóveda física.")