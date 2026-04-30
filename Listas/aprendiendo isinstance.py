#Aceptado! Este examen pondrá a prueba tu capacidad para usar el isinstance como un filtro de seguridad profesional
#Olvida el input() por un momento (para no pelear con el texto) y enfócate en la lógica de tipos.
#🏆 EXAMEN: "EL FILTRO DE LA BÓVEDA"
#El Escenario:
#Eres el programador de seguridad de la bóveda del BCP.
#El sistema recibe diferentes "paquetes" de datos
#Debes crear un código que identifique qué es cada cosa para decidir si lo deja pasar o lo bloquea.
#python
# Alex-the-cat9 | Examen de Validación isinstance()
# Día 17 de racha - Martes 21 de Abril
#Usa el código con precaución.
#🕵️ Reglas del Tech Lead:
#Precisión: No uses type() == int. Usa isinstance(dato, tipo).
#Limpieza: El código debe ser directo.
#Múltiple: En la Tarea 3, debes usar el paréntesis para evaluar dos tipos a la vez.

# Estos son los datos que llegan a la bóveda:
paquete_a = 500
paquete_b = ["llave_oro", "llave_plata"]
paquete_c = "CONTRASEÑA_ADMIN"
paquete_d = True

# --- TAREA 1: VALIDAR NÚMEROS ---
# Si paquete_a es un entero (int), imprime: "Monto verificado".
# [TU CÓDIGO AQUÍ]
if isinstance(paquete_a,int):
    print("monto vereficado")
else:
    print("Fallo necesita arreglo")


# --- TAREA 2: VALIDAR LISTAS DE ACCESO ---
# Si paquete_b es una lista (list), imprime: "Lista de llaves detectada".
# [TU CÓDIGO AQUÍ]
if isinstance(paquete_b,list):
    print("Lista de llaves detectada")
else:
    print("fallo encesita arreglo")


# --- TAREA 3: EL FILTRO MULTIPLE (Nivel Senior) ---
# Usa un solo isinstance() para verificar si paquete_c es un texto (str) 
# O un booleano (bool). Si es verdad, imprime: "Dato de identidad válido".
# Pista: Usa el paréntesis (tipo1, tipo2)
# [TU CÓDIGO AQUÍ]
if isinstance(paquete_c,(str,bool)):
    print("dato de identidad valido")
else:
    print("fallo en identidad")

# --- TAREA 4: DETECTAR INTRUSOS ---
# Crea un if que verifique si paquete_d NO es una lista (list).
# Pista: Usa 'if not isinstance(...)'
# Si se cumple, imprime: "Seguridad: El paquete D no es una lista peligrosa".
# [TU CÓDIGO AQUÍ]
if not isinstance(paquete_d, list):
    print("el paquete d no es una lista peligrosa")
else:
    print("fallo")



