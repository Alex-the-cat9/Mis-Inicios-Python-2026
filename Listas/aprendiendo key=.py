#🛡️ RETO: "EL ARCHIVO MÁS PESADO"
#El Escenario:
#Tienes una lista de archivos que se han descargado en tu sistema. El hacker ha intentado 
#camuflar el virus poniéndole un nombre muy largo para que no quepa en la pantalla de un terminal normal.
#Tu Misión:
#Tienes esta lista: 
descargas = ["foto.jpg", "notas.txt", "virus_encriptado_con_llave_maestra.exe", "web.html"]
#sa la función max() combinada con el parámetro key=len para encontrar automáticamente cuál es el nombre de archivo más largo.
#Imprime: "🚨 Archivo sospechoso por tamaño: [nombre_del_archivo]"
descargas.sort(key=len)
villano = len(descargas)
descargas.pop(villano - 1)
#🏆 EXAMEN: OPERACIÓN "FILTRO MAESTRO"
##Copia este código y completa las tareas. Recuerda: PROHIBIDO usar bucles for o if largos.
# Tienes que usar el poder de max(), min() o sort() con el parámetro key=.
#python
# Alex-the-cat9 | Examen de Reglas Especiales (key=)
# Día 17 de racha - Martes 21 de Abril

# --- ESCENARIO 1: LA CONTRASEÑA MÁS DÉBIL ---
# Tienes una lista de contraseñas. Encuentra la más CORTA (la más fácil de hackear).
passwords = ["admin123", "12345", "contraseña_ultra_segura_2026", "qwerty"]
# TAREA: Usa min() con key=len para encontrar la más débil
debil = min(passwords, key=len)
print(f"🚨 Alerta: La contraseña más débil es: {debil}")


# --- ESCENARIO 2: ORDENAMIENTO FORENSE ---
# Tienes una lista de archivos con mayúsculas y minúsculas desordenadas.
# El jefe quiere que los ordenes alfabéticamente pero IGNORANDO si son mayúsculas.
# Pista: Usa key=str.lower
archivos = ["zebra.exe", "Alpha.py", "backup.db", "Virus.sh"]
# TAREA: Usa .sort() con key=str.lower
# [TU CÓDIGO AQUÍ]
archivos.sort(key=str.lower)
print(f"📂 Archivos ordenados correctamente: {archivos}")



# --- ESCENARIO 3: EL PROCESO MÁS PESADO ---
# Tienes una lista de procesos. Encuentra el que tiene el nombre más LARGO.
procesos = ["svchost", "chrome", "system_idle_process_security_monitor", "taskmgr"]

# TAREA: Usa max() con key=len
pesado = max(procesos, key=len)
print(f"⚠️ Proceso sospechoso por longitud: {pesado}")
