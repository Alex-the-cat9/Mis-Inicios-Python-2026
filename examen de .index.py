#Alex:ahora un examen de .index
#maestro.IA:¡Oído cocina, Senior Alex! Este es tu Examen de Certificación .index().
#Este no es un reto cualquiera; es una simulación de Respuesta ante Incidentes. Si lo pasas, habrás cerrado la Fase 1 con una maestría total.
#🏆 EXAMEN: "OPERACIÓN CABALLO DE TROYA"
#El Escenario:
#Un virus ha entrado al servidor y ha infectado un archivo legítimo. Para ocultarse, el hacker ha movido
#el virus de posición varias veces.
#Tu misión es localizarlo, identificar qué archivos tiene a los lados (sus "vecinos") y eliminarlo.
# Alex-the-cat9 | Examen Final .index()
# Martes 21 de Abril - Día 16 de racha
#Reglas del Tech Lead:
#1:Precisión: No puedes escribir el número del índice a mano (ej. 2). Tienes que dejar que Python lo encuentre con .index().
#2:Seguridad: En la Tarea 4, usa el operador in o not in.
#3:Limpio: El código debe ser directo y sin vueltas innecesarias.

#Alex, si logras identificar al "vecino" del virus y borrar
#al intruso usando su índice, estarás listo para recibir tu acceso a la Fase 2 (Diccionarios).


servidor = ["index.php", "style.css", "VIRUS_TRICK", "database.sql", "main.py"]

# --- TAREA 1: LOCALIZACIÓN ---
# Encuentra el índice del archivo "VIRUS_TRICK" y guárdalo en una variable.
# [TU CÓDIGO AQUÍ]
ubicacion_virus = servidor.index("VIRUS_TRICK")#el index hace su trabajo y la variable ubicacion_virus atrapa lo que deja el index


# --- TAREA 2: ANÁLISIS DE VECINOS ---
# Usando el índice que encontraste, imprime qué archivo está JUSTO ANTES del virus.
# Pista: Usa servidor[indice - 1]
# [TU CÓDIGO AQUÍ]
print(f"el vecino isquierda:{servidor[ubicacion_virus - 1]}")#basicameente la ubicacion del virus fue 2 cuando imprimes/print algo de una lista lo haces asi print(servidor[1]) entonces:
print(f"el vecino de la derecha:{servidor[ubicacion_virus + 1]}")#lo que ise fue restar el numero de la ubicacion del virus -1 y +1 para ver sus vecinos



# --- TAREA 3: ELIMINACIÓN QUIRÚRGICA ---
# Usa .pop() con el índice que encontraste para borrar el virus.
# Pero guarda el nombre del virus eliminado en una variable llamada 'borrado'.
# [TU CÓDIGO AQUÍ]
borrado = servidor.pop(ubicacion_virus)#la variable borrado atrapa lo que deja pop

# --- TAREA 4: VERIFICACIÓN ---
# Si el virus ya no está en la lista, imprime "✅ SISTEMA DESINFECTADO".
# [TU CÓDIGO AQUÍ]
if "VIRUS_TRICK" not in servidor:#si "VIRUS_TRICK" no esta en el servidor entonces:
    print("SISTEMA DESINFECTADO")#SISTEMA DESINFECTADO puro codigo limpio ise nada de rodeos como me pidio mi maestro.ia