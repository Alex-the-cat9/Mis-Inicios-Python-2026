# Alex-the-cat9 | Scanner con Enumerate
#maestroIA: ¿Para qué sirve enumerate?
#Sirve para que el for te entregue dos cosas en cada vuelta:
#i: El índice (el número de asiento: 0, 1, 2...).
#x: El valor (lo que hay dentro del asiento).
#🛡️ El Código del "Rastreador GPS"
#red = ["PC_Admin", "PC_Invitado", "HACKER_PRO", "PC_Cajero"]
#
#print("--- 🔍 MAPEANDO POSICIONES DE RED ---")
#
# Se lee: "Para cada índice (i) y dispositivo (d) en la lista enumerada:"
#for i, d in enumerate(red):
#    if "HACKER" in d:
#        print(f"🚨 ¡OBJETIVO LOCALIZADO! En el puerto: {i} | Nombre: {d}")
#    else:
#        print(f"🟢 Escaneando puerto {i}... {d} está limpio.")
#Alex:si ya analize tu codigo y ya se para que sirve ahora dame un reto de for + enumerate para confirmar esto
#maestro.IA:💀 RETO: "CÓDIGO DE ACCESO SECCIONADO"
#El Escenario:
#Un hacker ha fragmentado una contraseña en 5 partes dentro de una lista. Para que la contraseña funcione,
#cada parte debe ir acompañada de su número de posición, de lo contrario, el sistema no la reconocerá.
#Tu Misión:
#Tienes esta lista: partes = ["Admin", "123", "Root", "S3cur3", "H4ck"].
#Usa un for con enumerate().
#Llama a tus variables temporales pos (para el índice) y token (para el valor).
#La Condición Especial:
#Si la posición (pos) es un número par (0, 2, 4...), imprime: "🔓 Fragmento [pos] validado: [token]".
#Si la posición es impar, imprime: "🔒 Fragmento [pos] encriptado...".
#(Pista de Senior: Para saber si un número es par, usa if pos % 2 == 0:).
# Alex-the-cat9 | Sincronizador de Tokens
partes = ["Admin", "123", "Root", "S3cur3", "H4ck"]
# [TU CÓDIGO AQUÍ]
for x, i in enumerate(partes):
    if x % 2 == 0:
        print(f"fragmento:{x} valido:{i}")
    else:
        print(f"fragmento:{x} encriptado")
