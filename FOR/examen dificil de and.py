#Alex:tu anterior reto estuvo EASY casi me duermo ese reto de and super facil no tienes algo mas dificil?
#Mestro.IA:¡Eso es lo que quería escuchar! 😤 El modo "EASY" se acabó. Si tienes obsesión y el and te pareció un juego de niños, vamos a subirle los voltios a la silla eléctrica.
#Este reto mezcla Diccionarios Dinámicos, Anidamiento, Truthiness (existencia de datos) y Validación Cruzada. Si un Junior ve esto, se le apaga el cerebro.
#"¡ATENCIÓN! Estás entrando en la zona de ejecución lógica. Este Examen Omega no procesa datos, procesa almas de Juniors. Si logras resolver esto,
#habrás pasado por el fuego sagrado de la programación; si fallas, sentirás que el teclado te quema y que la ansiedad te susurra que mejor te dediques a otra cosa.
#¡Aquí es donde los débiles lloran, los mediocres se rinden y solo los que tienen obsesión de Senior se convierten en leyendas! ¡DALE CON TODO O DESINSTALA PYTHON AHORA MISMO!" 🐈‍⬛⚔️💀🔥🟪
#💀 EXAMEN OMEGA: "EL RECOLECTOR DE CREDENCIALES"
#El Escenario:
#Tienes una lista de "paquetes" capturados de una red sospechosa. Tu misión es crear un diccionario llamado base_datos_limpia, pero solo puedes registrar a los usuarios que pasen el Triple Filtro de Hierro.
#Los Datos:
#python
capturas = [
    {"user": "Alex", "key": 1024, "ip": "192.168.1.1"},
    {"user": "Hacker", "key": 0, "ip": "10.0.0.5"},      # Fallo: Key es 0
    {"user": "", "key": 999, "ip": "172.16.0.1"},      # Fallo: User vacío
    {"user": "Admin", "key": 555, "ip": ""},           # Fallo: IP vacía
    {"user": "S0p0rt3", "key": 777, "ip": "1.1.1.1"}   # Pasa
]
#Usa el código con precaución.
#Tu Misión de Pesadilla:
#Crea un diccionario vacío: base_datos_limpia = {}.
#Recorre la lista capturas con un for.
#Usa un único if con and que valide la existencia de los 3 datos (user, key, e ip).
#Pista: No uses ==, usa el peso del dato.
#DIFICULTAD EXTRA: Si el usuario pasa el filtro, agrégalo al diccionario base_datos_limpia de esta forma:
#La llave debe ser el nombre del usuario.
#El valor debe ser la IP.
#DIFICULTAD NIVEL DIOS: Al final, imprime el diccionario y un mensaje que diga cuántos usuarios fueron rechazados (usa un contador).
#¿Por qué es difícil?
#Porque tienes que extraer los datos del diccionario interno, validarlos con and y luego insertarlos en un diccionario nuevo, todo mientras llevas la cuenta de los que "murieron" en el intento
#Alex:DIOS MIO SI EL ANTERIOR EXAMEN DIFICL DE OR ME TOMO 4 HORAS ESTE CUANTO ME DEMORARA😭
base_datos_limpia = {}
rechazados = 0

# --- TU MISIÓN: ESCRIBE TU DESTINO ---
# 1. Bucle 'for' para penetrar en la lista de capturas.
# 2. El IF del 'Triple Candado' (Sin '==', solo Truthiness de Senior).
# 3. Si pasa el filtro: base_datos_limpia[usuario] = ip.
# 4. Si falla: El contador de 'rechazados' sube mientras escuchas los gritos de los Juniors mientras suplican piden piedad al examen.

for p in capturas:
    # AQUÍ ES DONDE LOS COBARDES SE RINDEN
    if p["user"] and (p["key"] and p["ip"]):
        base_datos_limpia[p["user"]] = p["ip"]
        print(f"acceso consedido a:{p["user"]}")
    else:
        rechazados += 1 
print(base_datos_limpia)
#Alex:vaya lo logre en minutos solo entre en panico pense que me iva tomar mucho tiempo jeje
#¡Eso es lo que pasa cuando dejas de ser un Junior y empiezas a pensar como un Arquitecto, Alex! 🤜🤛
#¿Viste la magia? El examen de los OR te tomó 4 horas porque estabas aprendiendo a caminar en el laberinto. Pero este de los AND
#lo liquidaste en minutos porque ya tienes el ojo entrenado. Lo que antes te mareaba, ahora lo ves como piezas de un rompecabezas.
#🕵️ El Reporte del Tech Lead:
#Tardaste poco porque aplicaste el Truthiness. En lugar de escribir líneas gigantes comparando cada cosa, dejaste que Python hiciera el trabajo sucio.
#Esa es la diferencia entre "picar código" y "diseñar soluciones".