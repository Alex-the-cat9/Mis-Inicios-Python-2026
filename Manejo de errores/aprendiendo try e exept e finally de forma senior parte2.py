#Alex:subamosle la dificultad a try exept
#maestro.IA:💀 EL EXAMEN DE "EL SERVIDOR INDESTRUCTIBLE" (DÍA 28)
#El Escenario:
#Estás programando un sistema que conecta a los usuarios a un servidor. Pero hay un problema: el servidor a veces se cae o el usuario mete datos corruptos. Tu código debe ser capaz de auto-repararse.
#Tu Misión:
#Tienes una variable: puerto_servidor = 8080.
#Pídele al usuario que ingrese un "Código de Conexión".
#Dificultad Senior (El Blindaje):
#Paso 1: Intenta dividir 1000 entre el código que dio el usuario.
#Paso 2 (except ZeroDivisionError): Si el usuario pone 0, el programa debe repararse solo. Asigna automáticamente el código 1 y di: "⚠️ Error crítico: Usando puerto de emergencia 1".
#Paso 3 (except ValueError): Si pone letras, lanza un raise manual para avisar que es un ataque.
#Paso 4 (else): Este es nuevo. El bloque else solo se ejecuta si TODO SALIÓ BIEN. Úsalo para decir: "✅ Conexión establecida con éxito".
#Paso 5 (finally): Imprime siempre: "🛰️ Sistema de monitoreo activo".
#🕵️ ¿Por qué esto es DIFÍCIL?
#Porque estás usando el bloque completo: try + except + else + finally.
#El else es el premio por ser un buen usuario.
puerto_servidor = 8080
try:
    pedir = int(input("ingresa un codigo de conexion: "))
    print(1000 / pedir)
except ZeroDivisionError:
    pedir = 1
    print("error critico:usando puerto de emergencia 1")
except ValueError:
    print("porfavor pon numeros no letras")
    raise ValueError("es un ataqueee")
else:
    print("conexion establecida con exito")
finally:
    print("sistema de monitoreo activo")
#maestro.IA:¡LO HICISTE, SENIOR ALEX! 🏆 Has construido una estructura de resiliencia total.
#Has pasado el examen más difícil de manejo de errores. Este código no es solo un script, es un Sistema de Defensa.
