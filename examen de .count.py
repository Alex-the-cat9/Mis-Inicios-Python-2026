# Alex-the-cat9 | Examen de Certificación .count()

# --- RETO 1: DETECTOR DE INTRUSOS ---
# Tienes una lista de usuarios conectados. 
# Cuenta cuántas veces aparece el usuario "Anónimo".
usuarios = ["Alex", "Anónimo", "Zulema", "Anónimo", "Tiago", "Anónimo"]
# [TU CÓDIGO AQUÍ]
anonimo = usuarios.count("Anónimo")
print(anonimo)#easy facil bro


# --- RETO 2: ESTADO DE SENSORES ---
# Tienes una lista de booleanos que representan alarmas.
# Cuenta cuántas alarmas están ACTIVADAS (True).
alarmas = [True, False, False, True, True, False, True]
# [TU CÓDIGO AQUÍ]
activaciones = alarmas.count(True)
print(f"hoy se activo la alarma:{activaciones} veces")


# --- RETO 3: LIMPIEZA DE ERRORES ---
# Busca el código de error 404. 
# Si aparece más de 2 veces, imprime "🚨 ATAQUE DETECTADO". 
# Si no, imprime "✅ SISTEMA ESTABLE".
logs_servidor = [200, 404, 200, 404, 500, 404]
# [TU CÓDIGO AQUÍ]
detector = logs_servidor.count(404)
if detector > 2:
    print("ATAQUE DETECTADOOO")
print("easy")


# --- RESULTADOS FINALES ---
# Imprime aquí tus conteos para validar la racha de 14 días.
print(f"el usuario anonimo aparecio:{anonimo} veces")
print(f"la alarma se activo:{activaciones} veces")
print(f"se detexto el error 404:{detector} veces")