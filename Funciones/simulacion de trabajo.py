#Alex:ya ahora dame otro tiket de trabajo cualquiera
#maestro.IA:¡Recibido, Senior Alex! Veo que la obsesión sigue a tope. Vamos a subir el nivel: este ticket ya no es solo de "matemática", es de Estructura de Datos y Persistencia.
#Aquí tienes el Ticket #505. Olvida el paso a paso; el cliente solo te da el problema y tú entregas la solución.
#📩 TICKET DE TRABAJO #505 – DEPARTAMENTO DE LOGÍSTICA "NEBULA"
#Para: Sr. Arquitecto de Software Alex
#Asunto: Sistema de Gestión de Cargas Críticas
#Descripción:
#Necesitamos un software que registre la carga de nuestros drones de reparto. El sistema debe ser capaz de "crear" drones específicos y luego permitirnos añadir paquetes a su inventario.
#Requerimientos Técnicos:
#La Fábrica (El Motor): Crea una función que reciba el id_dron y la capacidad_maxima (en kg). Esta función debe devolver una herramienta para cargar paquetes.
#La Carga (Función Interna): Esta herramienta recibirá el nombre_paquete y su peso.
#Reglas de Negocio:
#Debes llevar la cuenta del peso_actual que lleva el dron (usa una variable dentro de la fábrica).
#Si el nuevo paquete excede la capacidad_maxima, se rechaza.
#Si el paquete pesa 0 o menos, se rechaza por error de sensor.
#La Respuesta (El Combo Return): El sistema debe devolver siempre:
#Un Booleano (Exito/Fallo).
#El peso_total acumulado que lleva el dron hasta ese momento.
#Una lista (o mensaje) con el estado: "CARGADO", "SOBREPESO" o "ERROR_SENSOR".
#Prueba de Entrega:
#Crea el Dron-Alpha con capacidad de 20kg.
#Carga un paquete de 10kg.
#Carga otro de 5kg.
#Carga uno de 10kg (Este debería fallar por sobrepeso).
#Muestra los resultados de cada intento para que el departamento de logística vea que el return está enviando los datos correctos.

#🕵️ Pista de Senior (Sin paso a paso):
#Recuerda que para que el peso se mantenga "vivo" dentro del dron cada vez que lo llamas, la variable debe estar en la función padre.
#Alex, el cliente espera un software que no pierda datos entre cada paquete. ¡Demuestra esa arquitectura! 🐈‍⬛⚔️🟩🔥🦾
#¿Listo para el Ticket #505? Solo los que dominan el return y las funciones anidadas sobreviven a este.
def crear_dron(id_dron, capacidad_maxima):
    peso_actual = 0
    def la_carga(nombre_paquete, peso):
        nonlocal peso_actual# linea con ayuda
        if peso == 0:
            return False, peso_actual, "ERROR_SENSOR"
        if (peso + peso_actual) > capacidad_maxima:#linea con ayuda
            return False, peso_actual, "SOBREPESO"
        else:
            peso_actual += peso
            return True,  peso_actual, "CARGADO"
    return la_carga
capacidad_maxima = crear_dron(122,20)
nombre_paquete = input("el nombre del producto:  ")
peso = int(input("que peso tiene este paquete?: "))
print("enviando....")
exito, peso, mensaje = capacidad_maxima(nombre_paquete,peso)
if exito:
    print(f"su paquete fue {mensaje} el nombre es:{nombre_paquete} su peso:{peso}")
else:
    print(f"su paquete fue rechazado por {mensaje}")
nombre_paquete = input("el nombre del producto:  ")
peso = int(input("que peso tiene este paquete?: "))
print("enviando....")
exito, peso, mensaje = capacidad_maxima(nombre_paquete,peso)
if exito:
    print(f"su paquete fue {mensaje} el nombre es:{nombre_paquete} su peso:{peso}")
else:
    print(f"su paquete fue rechazado por {mensaje}")



