#Alex:todavia no ya no somos juniors ahora va cambiar dame un trabajo real basado en return como
#si alguien de verdad me lo pidiera no paso a paso quiero prepararme porque cuando ese dia llegara no le dire que me diga paso a paso como me lo dices

#maestro.IA:Esa es la mentalidad de un Senior Alex. 🤜🤛 Se acabó el entrenamiento con rueditas. En el mundo real, un cliente o tu jefe en el BCP no te va a decir
#"usa un if" o "haz un return". Te van a dar un problema de negocio y tú verás cómo lo resuelves.
#Aquí tienes tu primer Ticket de Requerimiento Real. Prepárate, porque así es como llega el trabajo a la oficina.

#📩 TICKET DE TRABAJO #402 – DEPARTAMENTO DE SEGURIDAD DIGITAL
#Para: Sr. Desarrollador Alex
#Asunto: Sistema de Validación de Transacciones de Alto Riesgo
#Descripción:
#Necesitamos un motor lógico que decida si una transferencia de dinero debe ser procesada o bloqueada. El sistema debe ser una "fábrica de validadores" porque cada tipo de moneda
#(Soles, Dólares, Cripto) tiene límites diferentes.
#Requerimientos Técnicos (Lo que el cliente espera):
#El Motor: Una función que reciba el limite_maximo de la moneda y devuelva una herramienta de validación.
#La Validación: La herramienta devuelta debe recibir el monto y el nombre_usuario.
#Reglas de Negocio:
#Si el monto supera el limite_maximo, la transacción se rechaza.
#Si el nombre_usuario está vacío o es un espacio, se rechaza por anonimato.
#Si todo está en orden, se acepta.
#La Respuesta: No queremos mensajes de texto sueltos. El sistema debe devolver obligatoriamente un "combo" con:
#Un Booleano.
#Un código de estado.
#El monto final con una comisión del 5% aplicada (solo si es exitosa).
#Prueba de Entrega:
#Crea un validador para Dólares con un límite de $5000. Intenta procesar una transacción de $6000 y otra de $1000 con el usuario "Alex". Muestra los resultados finales.
#Alex, aquí no hay pistas. El cliente solo quiere que el código funcione y que devuelva los datos correctos para poder guardarlos en su base de datos.
#"En la oficina nadie te explica el código, solo te explican el problema. ¡Demuestra que ya eres el arquitecto!"
#¿Listo para entregar este software profesional? Solo los Seniors terminan el día con un código de este calibre.

def limite_maximo(limite_maximo):
    def validacion(nombre_usuario, monto):
        if monto > limite_maximo:
            return False,"transaccion rechazada por exeder el limite maximo"
        if nombre_usuario == " " and len(nombre_usuario) == 0:
            return False, "rechazado por anonimato"
        else:
            return True, "codigo de estado:1921", monto
    return validacion
limite = limite_maximo(5000)
nombre = input("ingrese su nombre de usuario:")
monto = int(input("ingrese su monto:"))
exito, valor_monto = limite(nombre, monto)#con ayuda esta linea
if exito:#con ayuda esta linea
    comision = monto * 0.05
    monto_final = monto - comision
    print(f"su entrega a sido exitosa se le cobrara un 5% de comision a su monto:{monto_final}")
else:
    print(f"su trassacion a sido rechazada por un motivo")
    


