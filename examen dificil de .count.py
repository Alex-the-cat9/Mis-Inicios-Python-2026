# Alex-the-cat9 | Examen de Élite .count()

logs_sucios = ["admin", 404, "VIRUS", "404", 404, "virus", "VIRUS", 200, "VIRUS"]

# --- RETO 1: EL DOBLE AGENTE ---
# Cuenta cuántas veces aparece el número REAL 404.
# Y cuenta cuántas veces aparece el texto "404".
# (Demuestra que el detective sabe distinguir tipos de datos).
conteo_numero = logs_sucios.count(404)
conteo_texto = logs_sucios.count("404")
# --- RETO 2: LA AMENAZA FANTASMA ---
# El hacker escribió "VIRUS" y "virus". 
# Queremos el CONTEO TOTAL de virus sin que importe si es mayúscula o minúscula.
# Pista: No puedes usar .lower() directamente en la lista, pero puedes usar lo que aprendiste.
# [TU CÓDIGO AQUÍ]
virus_minuscula = logs_sucios.count("VIRUS")
virus_MAYUSCULA = logs_sucios.count("virus")
# --- RETO 3: EL CÓDIGO DE DEFENSA ---
# Si el total de "VIRUS" (mayúsculas + minúsculas) es mayor a 2 
# Y el conteo de números 404 es exactamente 2:
# Imprime "🚨 PROTOCOLO DE PURGA ACTIVADO"
# De lo contrario, imprime "🛡️ VIGILANDO..."
# [TU CÓDIGO AQUÍ]

total_VIRUS = virus_minuscula + virus_MAYUSCULA
if total_VIRUS > 2 and conteo_numero == 2:
   print("PROTOCOLO DE DEFENSA")
else:
 print("TODO SEGURO:)")
