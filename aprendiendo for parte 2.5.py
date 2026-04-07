#Tú escribiste: if Alex in mochila == "diamante" or "anillo de oro":
#El problema del in mochila: Dentro de un bucle for Alex in mochila:, la variable Alex ya es el objeto. No necesitas volver a preguntar si está en la mochila; Python ya sabe que lo sacó de ahí.
#La trampa del or: Al poner or "anillo de oro", Python no entiende que estás comparando. Para Python, cualquier texto solo (como "anillo de oro") siempre es Verdad, por eso te decía que vendía todo, ¡hasta el barro!
mochila = ["madera", "piedra", "anillo de oro", "diamante", "palo"]
for Alex in mochila:
    if Alex  == "diamante" or Alex == "anillo de oro":
        print(f"alex vendio su: {Alex} a 100$")
    else:
        print(f"alex guardo su:{Alex} no vale nada")
#¡Eso es, Alex! Ahora sí el código es impecable. 🏆
#Has aplicado la lógica correcta:
#Comparación doble: Alex == "diamante" or Alex == "anillo de oro" es la forma exacta en que Python entiende que quieres filtrar esos dos objetos específicos.
#F-strings limpias: El uso de {Alex} dentro de los prints hace que el mensaje sea dinámico y profesional.
#Lógica perfecta: Ahora, si lo corres, verás que solo vende lo valioso y guarda lo demás. ¡El mercader ya no te va a estafar!
