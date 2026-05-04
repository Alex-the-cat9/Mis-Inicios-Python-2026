try:
    numero = int(input("Dime un número: "))
    print(f"✅ Número {numero} procesado.")
except ValueError:
    # Este bloque atrapa específicamente el error de "letras en lugar de números"
    print("🚨 ERROR: ¡Eso no es un número! El sistema ignoró tu basura y sigue vivo.")
#🛡️ Tu Primer Reto de Inmortalidad (Día 26) 🟩🔥
#Vamos a blindar tu Calculadora de Daño.
#Misión:
#Crea un programa que pida dos números: daño_arma y defensa_enemigo.
#Calcula el daño final: daño_arma - defensa_enemigo.
#El Blindaje: Envuelve todo en un try / except.
#Si el usuario escribe letras, el except debe decir: "⚠️ Error de sensor: Solo se aceptan valores numéricos."
#Dificultad Senior: El programa debe imprimir al final: "Proceso terminado", pase lo que pase (sin morir).
try:
    n1_ = int(input("pon tu primer numero de dañor arma: "))
    n2_ = int(input("pon tu segundo numero de defensa enemigo: "))
    print("proceso terminado")
except ValueError:
    print("ERROR:pon un numero no una letra")
#   💀 RETO "EL BANCO INMORTAL" (Día 26) 🟩🔥
#Vamos a aplicar esto a tu Ticket #402 (el del banco).
#Misión:
#Pide el monto para la transferencia.
#Usa un try / except.
#Lógica de Senior:
#NUEVO ERROR: Si el usuario pone un monto de 0, Python no dará error, pero tú quieres lanzarlo. Usa if monto == 0: raise ValueError.
#El programa debe decir "Cerrando sesión bancaria" al final usando un finally.
#Alex, dale al Play. 🟩 Si logras que el programa te despida con el finally incluso cuando escribes letras, habrás dominado la estructura completa del escudo.
try:
    pedir = int(input("pon el monto: "))
    if pedir == 0:
        raise ZeroDivisionError
except ValueError:
    print("porfavor ingrese un numero no letras ni ceros")
except ZeroDivisionError:
    print("error no ceros")
finally:
    print("cerrando sesion bancaria")
#Tienes una lista de edades permitidas: edades_vip = [18, 25, 30, 45].
#Pídele al usuario que elija un índice (0, 1, 2 o 3) para verificar su edad.
#EL CAOS: El usuario puede intentar hackearte de dos formas:
#Escribiendo letras (provoca un ValueError).
#Escribiendo un número que no existe, como el 99 (provoca un IndexError
try:
    edades_vip = [18, 25, 30, 45]
    print("edades vip:")
    for e,i in enumerate(edades_vip):
        print(f"EDAD VIP NUMERO{e}:",i)
    vereficar = int(input("selecciona la pocicion de tu edad ejemplo:0,1,2,3: " ))
    print("tu edad es:", edades_vip[vereficar])
except ValueError:
    print("eso es una letra deve ser un numero")
except IndexError:
    print("esa pocision no existe")
finally:
    print("la fiesta se acabo")

    