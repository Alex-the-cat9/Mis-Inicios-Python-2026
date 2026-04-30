#💀 EXAMEN OMEGA: "EL INFILTRADO EN LA BASE DE DATOS"
##El Escenario:
#Has interceptado el diccionario de un servidor enemigo. Tienes que realizar una limpieza quirúrgica usando in, and, or y del.
#python
# Alex-the-cat9 | OPERACIÓN OMEGA: DICCIONARIOS
# Si fallas, el rastro del hacker se queda en el sistema.

servidor = {
    "admin": "Alex",
    "ip_origen": "192.168.1.100",
    "puerto": 80,
    "virus": "troyano.exe",
    "estado": "infectado"
}

black_list = ["192.168.1.100", "10.0.0.1", "666.666.666.1"]

# --- TU MISIÓN DE PESADILLA ---

# 1. DETECCIÓN DOBLE: 
#    Crea un IF que verifique si la llave "ip_origen" existe EN el servidor 
#    Y ADEMÁS (and) si su valor está DENTRO de la 'black_list'.
#    Si es verdad, imprime: "🚨 AMENAZA CRÍTICA: IP NEGRA DETECTADA".

# 2. PURGA SELECTIVA:
#    Si la llave "virus" existe OR el "estado" es igual a "infectado":
#    - Elimina la llave "virus" del diccionario (usa 'del servidor["virus"]')
#    - Cambia el valor de "estado" a "LIMPIO".
#    - Imprime: "🛡️ Sistema purgado con éxito".

# 3. VERIFICACIÓN FINAL:
#    Al final, imprime el diccionario 'servidor' para demostrar que el virus ya no existe.
if "ip_origen" in servidor and servidor["ip_origen"] in black_list:
    print("AMENAZA CRITICA:IP NEGRA DETECTADA")

if "virus" in servidor:
    del servidor["virus"]#aprendi del muy rapido solo me dijieron que es igual a un remove para listas
if "estado" in servidor and servidor["estado"] == "infectado":
    servidor["estado"] = "LIMPIO"
print(servidor)
