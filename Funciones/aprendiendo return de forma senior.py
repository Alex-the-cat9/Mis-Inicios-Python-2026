#🛡️ Reto de Reconexión: "El Generador de Tokens" (Día 24)
#En ciberseguridad, un token es una clave secreta que una función te entrega para que puedas entrar.
#Misión:
#Crea una función llamada generar_token.
#Debe recibir un nombre.
#Debe return el nombre sumado a un número secreto (ejemplo: nombre + "777").
#IMPORTANTE: Fuera de la función, guarda ese resultado en una variable llamada mi_llave.
#Imprime: f"Llave de acceso creada: {mi_llave}"
def generar_token(token):
    token = token + "777"
    return token
mi_token = generar_token("Alex")
print(f"llave de acceso creada:{mi_token}")
#💀 EL RETO DEL "FILTRO DE SEGURIDAD" (Nivel Grey Hat)
#Vamos a complicarlo un poco para que el cerebro termine de despertar.
#Misión:
#Crea una función llamada limpiador_de_usuarios.
#Debe recibir un nombre.
#Lógica interna:
#Si el nombre tiene más de 10 letras (len()), debe hacer return "ERROR: NOMBRE MUY LARGO".
#Si no, debe hacer return nombre.upper() (el nombre en mayúsculas).
#Fuera de la función:
#Llama a la función dos veces: una con tu nombre y otra con un nombre inventado gigante (ej: "Hacker_Ruso_Super_Malo_99").
#Imprime ambos resultados.
#Alex, dale al Play. 🟩 Aquí estás usando el return para enviar dos tipos de paquetes diferentes según lo que pase adentro. ¡Eso es inteligencia de software!
def limpiador_de_usuarios(limpiar):
    if len(limpiar) > 10:
        print("ERROR:NOMBRE MUY LARGO")
    else:
        return(limpiar.upper())
print(limpiador_de_usuarios(mi_token))
print(limpiador_de_usuarios("Hacker_Ruso_Super_Malo99"))
#💀 EXAMEN OMEGA: "EL REPARTIDOR DE CREDENCIALES"
#El Escenario:
#Necesitas un sistema que limpie las contraseñas de los usuarios. Si la contraseña es débil, la función debe avisar; si es fuerte, debe devolverla "encriptada".
#Tu Misión:
#Crea la función procesar_password(clave).
#Lógica Interna (El Mensajero):
#Si la clave tiene menos de 5 letras, debe hacer return "DÉBIL".
#Si la clave es igual a "12345", debe hacer return "RECHAZADA".
#Si no es ninguna de las anteriores, debe hacer return f"#{clave}#" (esto simula una encriptación).
#Fuera de la función (El Cliente):
#Pídele al usuario una clave con un input.
#Llama a la función y guarda el paquete en una variable llamada resultado.
#Toma una decisión:
#Si el resultado es "DÉBIL" o "RECHAZADA", imprime: "🚫 Error: Intente con otra clave".
#Si el paquete trae la clave encriptada, imprime: f"✅ Clave guardada con éxito: {resultado}".
#🕵️ Reglas de Oro del Tech Lead:
#PROHIBIDO usar print dentro de la función. La función solo debe fabricar el paquete y lanzarlo con return.
#RECUERDA: El return es el que saca el dato de la oficina para que tú lo uses en el if de afuera.
def procesar_password(clave):
    if len(clave) < 5 or clave == "12345":
        return "CLAVE:DEBIL"
    else:
        return f"#{clave}# clave fuerte encriptada"
poner_clave = input("pon tu clave y vereficaremos si es debil o no: ")
print(procesar_password(poner_clave))#perdon por usar print aqui pero no se podia sin ese print
#maestro.IA:Ahora aprenderemos sobre las funciones dentro de las funciones
def usuario(nombre):
    print(f"🛰️ Registrando a: {nombre}")
    
    # Esta es la función interna (el motor)
    def asignar_rango(puntuaje):
        if puntuaje < 10:
            return f" {nombre}, tienes un rango MEDIO"
        else:
            return f" {nombre}, tienes un rango ALTO"
    
    # ¡ESTE ES EL SECRETO!: Devolvemos la función entera
    return asignar_rango 

# 1. Creamos el perfil de Alex
perfil_alex = usuario("Alex")
ver_puntuaje = int(input("que puntuaje tienes? : "))
print(perfil_alex(ver_puntuaje))
#💀 RETO: "EL GENERADOR DE AGENTES"
#El Escenario:
#Necesitas una fábrica que cree "Agentes de Seguridad". Cada agente debe tener un nombre de código y un nivel de acceso secreto.
#Tu Misión:
#Crea la función padre: crear_agente(codigo_secreto).
#Dentro, crea la función hijo: verificar_acceso(nombre, password).
#Lógica del Hijo:
#Si la password es igual al codigo_secreto del padre, debe return dos cosas: True y un mensaje: "🔓 ACCESO TOTAL".
#Si no, debe return dos cosas: False y un mensaje: "🚫 INTRUSO DETECTADO".
#La función padre debe hacer return de la función hijo.
#En el mundo real (Fuera de las funciones):
#Crea un agente llamado agente_shadow usando la fábrica con el código "1010".
#Usa un input para pedir la contraseña.
#Llama a agente_shadow("Alex", password_del_input).
#CUIDADO: Como la función devuelve dos cosas, recíbelas en dos variables: exito, mensaje = agente_shadow(...).
#mprime el mensaje.
#🕵️ ¿Por qué este reto es brutal?
#Usas Clausuras (el hijo recuerda el código del padre).
#Usas Desempaquetado (recibes dos paquetes del return).
#Usas Seguridad Dinámica.
def crear_agente(codigo_secreto):
    def vereficar_acceso(nombre, password):
        if password == codigo_secreto:
            return True, "ACCESO TOTAL"
        else:
            return False, "INTRUSO DETECTADO"
    return vereficar_acceso
agente_shadow = crear_agente(1010)
pedir = int(input("ingrese contraseña: "))
print(agente_shadow("Alex", pedir))
#Alex:esto se esta poniendo aburrido vamos a hackear mi propio programa
intentos = 0
#print(type(agente_shadow("Alex", pedir)))clase tupla
for i in range(10000):
    intentos += 1
    print(agente_shadow("Alex", intentos))
    if "ACCESO TOTAL" in agente_shadow("Alex", intentos):
        print(f"contraseña decifrada la contraseña es:{intentos}")
        break 
#Alex:mi primer Credential Cracker
