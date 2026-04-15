#💼 PRUEBA TÉCNICA: "El Optimizador de Pedidos de Amazon-Alex"
#El Problema:
#Tienes un almacén de entregas. Los camiones solo pueden cargar el último paquete que llegó (porque es el que quedó más cerca de la puerta), pero a veces llega un cliente VIP que exige que su paquete salga de inmediato, sin importar dónde esté.
#Tu Misión:
#Estado del Almacén: Comienza con 4 paquetes en el sistema (ponle nombres de productos).
#Operación Normal: Crea un sistema que "despache" (saque del sistema) el último paquete y lo muestre en pantalla.
#Operación VIP: Permite que un operario elija una posición específica (el índice) para sacar un paquete urgente y moverlo a una lista especial llamada entregas_prioritarias.
#Seguridad de Datos: Si el operario intenta sacar un paquete de una posición que no existe o si el almacén está vacío, el programa debe avisar y no romperse (puedes usar un if con el len).
#Reporte Final: Al terminar, el programa debe mostrar cuántos paquetes quedan en el almacén y cuál fue el último paquete VIP que se procesó.
import time
almacen = ["cepillo", "arma", "bombas", "mama coco"]
entregas_prioritarias = []
print("se entregara el ultimo paquete cada cierto tiempo vamos trabajar lo mas rapido que podamos")
while len(almacen) > 0 :
    for i in almacen:
        print(i)
    usuario_vip = input("deseas interferir y que tu paquete llege lo mas rapido posible? si/no : ")
    if usuario_vip == "si":
        for i in enumerate(almacen):
            print(i)
        
        preguntar = int(input("que numero es su paquete?: "))
        if preguntar < len(almacen):
            print("su paquete esta saliendo de inmediato.....")
            time.sleep(5)
            print("listo que tenga un buen dia")
            print(f"el paquete fue entregado con exicto y es:{almacen[preguntar]} y fue a causa de un vip se va a la lista de entregas prioritarias")
            entregas_prioritarias.append(almacen.pop(preguntar))
            continue

        else:
            print("usuario vip ese numero de paquete no ay en este almacen bueno seguiremos entregando paquetes a usuarios no vip")
    print("entregando otro paquete....")
    time.sleep(5)
    print(f"el paquete fue entragado con exicto y es:{almacen.pop()}")
print(f"entregamos todos los paquetes quedan:{len(almacen)} en el almacen")
print("las entregas de los vips fue:")
for e in entregas_prioritarias:
    print(e)
# --- EL DEBATE TÉCNICO ---
# Socio IA: "Alex, tienes un bug. Si el VIP se lleva el último paquete, 
# el pop() final de la línea 35 fallará. Ponle un IF para protegerlo."

# Alex (El Alumno): "Tengo una idea mejor maestro... ¿Y si usamos CONTINUE?"
# El razonamiento de Alex: Al usar 'continue', si el VIP se lleva un paquete, 
# el programa salta el resto de la vuelta y regresa al inicio del 'while'. 
# Es más limpio, tiene menos líneas y evita el error de raíz.

# --- CONCLUSIÓN ---
# El alumno superó al maestro en simplicidad y limpieza de código. 
# El uso de 'continue' hace que el flujo sea más rápido y profesional.
#exacto yo dije que usaramos continue le dije a mi maestro que escribiera algunos # porque me da flojera escribirlos todos y a mi me gusta escribir codigos no mucho texto pero cuando se trata de explicar mi codigo si me gusta jejeje
#le dije al mi maestro que los examenes dificiles lo isiera mas complicado y con menos explicaciones como si una persona normal me lo dijiera que lo isiera oh como una empresa le diria a un programador porque yo quiero ser uno
#al principio me dolia la cabeza menos texto y pense en rendirme pero tuve determinacion y me tarde 2 horas pero lo logre amigos de git hub