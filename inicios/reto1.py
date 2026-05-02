#RETO 1: El Filtro de Bots 🤖
#Lógica: Queremos que Alex y el Gato Ninja pasen, pero los que dicen "Bot" no.

#usuarios = ["Alex", "Bot_1", "Gato_Ninja", "Bot_2"]

#usuarios = ["Alex", "Bot_1", "Gato_ninja", "Bot_2"]#lista de los usuarios
#human = []#humanos
#Bot = []#Bots malvados
#for i in usuarios:#bucle for i in usuarios
#    if "Bot" in i:#si "Bot" not esta in/en i(entonces tienes que hacer esto:)
#        Bot.append(usuarios.pop("bot" in i))
#        
#        
#print(usuarios)
#print(human)
#Alex: me rindo no puedo llevo 2 horas haciendo este codigo y no me sale
#usuarios = ["Alex", "Bot_1", "Gato_ninja", "Bot_2"]
#humanos = []
#bots_malvados = []
#
#for i in usuarios:
#    if "Bot" in i:
#        # Si la etiqueta dice "Bot", va a la lista de malvados
#        bots_malvados.append(i)
#    else:
#        # Si no la tiene, es un humano seguro
#        humanos.append(i)

## --- RESULTADOS ---
#print(f"Humanos detectados: {humanos}")
#print(f"Bots capturados: {bots_malvados}")
#Alex:Mastro deme otro reto el reto1 no pude completarlo
#socioIA:El Validador de Presupuesto" 💰📦
#El Problema:
#Alex tiene una lista de precios de los paquetes que quiere enviar, pero solo tiene $100 dólares en su cuenta. Si el paquete cuesta más de $100, no puede salir del almacén.
#osea solo tiene 100 pero cada compra lo resta oh sigue teniendo 100
#¡Qué buena pregunta! Has detectado la diferencia entre un filtro simple y un sistema de gastos real. 🧠✨
#Para que este reto sea nivel Senior, vamos a hacerlo con un sistema de gastos. Es decir:
#Alex empieza con $100.
#Cada vez que compra algo, ese dinero se resta de su saldo.
#Si el siguiente paquete cuesta más de lo que le queda, no puede comprarlo.
#🛠️ El Mapa de Lógica para Alex:
#Saldo inicial: Crea una variable dinero = 100.
#La Lista: precios = [20, 50, 40, 10]
#dinero = 100
#lista_de_precio = [20, 50, 40, 10]
#print("Alex comprara sus cosas y va pasando")
#for i in lista_de_precio:
#   if dinero > i:
#      dinero = dinero - i
#      print("comprado")
#   else:
#      print("saldo insuficiente") 
#Alex:Dios este reto tampoco lo pude hacer bien bueno la tercera es la vencida
#socioIA: "El Firewall de Alex" 🛡️💻
#El Problema:
#Tienes una lista de dispositivos que intentan conectarse a tu red wifi. Algunos son conocidos y otros son sospechosos.
dispositivos = ["Alex", "Alex2", "Alex3", "Bot no alex"]
print("--------El firewall de Alex------")
import time
vereficacion = len(dispositivos)
print("detentando dispositivoss.....")
time.sleep(3)
for i in dispositivos:
    if "Bot"in i:
        print("Sacando a la basura")
        dispositivos.remove(i)
print("Alex que quedaron vivos:")
for e in dispositivos:
    print(e)
#Alex:Ganeee
