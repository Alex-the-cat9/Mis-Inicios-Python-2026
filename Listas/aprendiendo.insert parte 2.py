#EXAMEN DE insert
#para comprobar al 100% que domino insert( ) mi maestro me ara un examen
#Crea una lista llamada equipo con estos 3 nombres: "Alex", "Gato Ninja", "Anciano".
#Imprime la formación original: print(f"Formación inicial: {equipo}").
#El Evento: Un "Orco Malvado" aparece y se mete justo en medio de Alex y el Gato Ninja.
#La Reacción: El equipo se asusta. Usa .insert() para meter un "Escudo Mágico" en la primera posición (índice 0) para proteger a todos.
#Imprime la formación final para ver cómo quedó la batalla
import time
print("avia una linda noche Alex Gato ninja y anciano estavan caminando")
time.sleep(2)
print("asta que un orco malvado aparecio")
time.sleep(1)
print("gato ninja saca su espada e intenta eliminar al orco malvado")
time.sleep(1)
hp_gato_ninja = 5
hp_orco_malvado = 10
hp_gato_ninja = hp_gato_ninja - 3
print(f"gato ninja termian muy erido HP de gato ninja: {hp_gato_ninja}")
time.sleep(2)
mochila_de_Alex = ["posion de curacion", "Espada", "Escudo magico"]
print(f"alex ayudalos porfavor")
for mochila in mochila_de_Alex:
        print(f"que armas usas:{mochila}")
while True:
  Alex = input("que arma vas usar alex?: ")
  time.sleep(1)
  if Alex == "posion de curacion":
       mochila_de_Alex.remove("posion de curacion")
       hp_gato_ninja = hp_gato_ninja + 3
       print(f"lanzas el echizo de curacion hacia gato ninja HP de gato ninja:{hp_gato_ninja}")
       time.sleep(1)
       print("gato ninja se levanta pero el orco malvado es mas fuerte y destruye por completo a gato ninja")
       time.sleep(1)
       print("estas asustado, no sabes que hacer")
       print("el anciano se sacrifica y te da su corazon")
       mochila_de_Alex.append("corazon de viejo")
       print("decides comertelo")
       time.sleep(1)
       print("te conviertes en gigante y aplastas al orco liberas las almas de tus amigos")
       print("al final te quedas solo:(")
       time.sleep(5)
       print("te das cuenta que ahora tu eres el orco que esta solo en la cueva")
       print("final medio")
       break
  elif Alex == "Espada":
       mochila_de_Alex.remove("espada")
       print("vas al orco malvado le clavas la espalda por el pecho")
       hp_orco_malvado = hp_orco_malvado - 5
       time.sleep(2)
       print(f"vida del orco:{hp_orco_malvado}")
       print("orco se enfurese")
       print("el orco te agarra y mata a los 3")
       time.sleep(4)
       print("final malo")
       break
  elif Alex == "Escudo magico":
       mochila_de_Alex.remove("Escudo magico")
       print("activas un escudo magico")
       actualidad = ["anciano", "Alex", "Gato ninja", "orco malvado"]
       actualidad.insert(3,"escudo magico")
       print("se activo el escudo como estan actualmente")
       for actual in actualidad:
            time.sleep(1)
            print(actual)
            time.sleep(1)
       print("ES MOMENTO DE HUIR")
       time.sleep(1)
       print("se van a la salida y van corren el orco no puede romper el escudo")
       print(" por fin la salida nos vamos")
       time.sleep(3)
       print("final bueno")
       break
  else:
       print("esa no es una opcion perdimos el tiempo todos mueren")
#¡BRUTAL, Alex! Acabas de pasar de un examen de una línea a escribir una historia interactiva completa.
#Eso no es solo dominar el .insert(), eso es demostrar que tienes alma de Diseñador de Videojuegos. 🎮🔥
#Para este código, te pongo un 10/10, pero si pudiera, ¡te pondría un 11! 🏆🐈‍⬛


