from Invocador import Minion, Invocador
from Retodificil import Mago, Asesino, Curandero
from random import choice, choices
from sys import exit
def eleccion_de_Personajes_comunes(Personaje):
    if Personaje == "mago":
        nombre = input("eligue su nombre: ").lower()
        if len(nombre) <= 1:
             print("nombre normal por nombre invisible")
             nombre = "Alex"
        return Mago(nombre, 100)
    elif Personaje == "asesino":
        nombre = input("eligue su nombre: ").lower()
        if len(nombre) <= 1:
             print("nombre normal por nombre invisible")
             nombre = "Pepe"
        return Asesino(nombre, 100)
    elif Personaje == "curandero":
        nombre = input("eligue su nombre: ").lower()
        if len(nombre) <= 1:
             print("nombre normal por nombre invisible")
             nombre = "gato_ninja"
        return Curandero(nombre, 200)
def eleccion_de_Personajes_enemigos():
     enemigo_mago = Mago("pepito", 100)
     enemigo_curandero = Curandero("angel", 200)
     enemigo_asesino = Asesino("alexis", 100)
     enemigo_Invocador = Invocador("gato_ninja", 100)
     Enemigos = [enemigo_mago, enemigo_curandero, enemigo_asesino, enemigo_Invocador]
     Equipo_enemigo = choices(Enemigos, weights=[30,20,40,10], k=3)
     return Equipo_enemigo
while True:
    Personajes = ["mago", "asesino", "curandero"]
    equipo:list[Mago| Asesino | Curandero | Invocador | Minion] = []
    user1 = input("elige tu personaje Mago asesino o curandero: ").lower()
    if len(user1) <= 1 or user1 not in Personajes:
            print("ERROR:personaje vacio")
            continue
    mi_personaje1 = eleccion_de_Personajes_comunes(user1)
    user2 = input("elige tu personaje dos Mago asesino o curandero: ").lower()
    if len(user2) <= 1 or user2 not in Personajes:
            print("ERROR:personaje vacio")
            continue
    mi_personaje2 = eleccion_de_Personajes_comunes(user2)
    user3 = input("elige tu personaje tres  Mago asesino o curandero: ").lower()
    if len(user3) <= 1 or user3 not in Personajes:
            print("ERROR:personaje vacio")
            continue
    mi_personaje3 = eleccion_de_Personajes_comunes(user3)
    try:
        equipo.append(mi_personaje1)
        equipo.append(mi_personaje2)
        equipo.append(mi_personaje3)
        break
    except Exception:
        print("error personaje no esta en la lista")
def turno_de_enemigos(equipo_rival, equipo_enemigo):
     if len(equipo_rival) <= 0:
          print("GANARON LOS ENEMIGOS")
          exit()
     print("--------------------------------------")
     enemigo_jugar = choices(equipo_enemigo, k=1)[0]
     if enemigo_jugar.nombre == "angel":
          curar = choices(equipo_enemigo, k=1)[0]
          enemigo_jugar.atacar(curar)
          print(f"el curandero: {enemigo_jugar.nombre} del equipo enemigo CURO A {curar.nombre} DE SU EQUIPO")
          return
     print("el enemigo que va jugar es:")
     print(repr(enemigo_jugar))
     enemigo_de_enemigo = choices(equipo_rival, k=1)[0]
     print("atacara a:")
     print(enemigo_de_enemigo)
     print("---------------------------------------")
     if enemigo_jugar.nombre == "gato_ninja":
          resuelto = choices(["invocar", "atacar"], weights=[10, 90], k=1)[0]
          if resuelto == "invocar":
               enemigo_jugar.invocar(equipo_enemigo)
               print("el invocador del equipo enemigo ah invocado un minion")
               return
          else:
               enemigo_jugar.atacar(enemigo_de_enemigo)
               print(f"el invocador del equipo enemigo ataco a:{enemigo_de_enemigo.nombre}")
               if enemigo_de_enemigo.vida <= 0:
                    equipo_rival.remove(enemigo_de_enemigo)
                    print("----------------------------------")
                    print(f"MURIO:{enemigo_de_enemigo.nombre}")
                    print("----------------------------------")
               return
     daño = enemigo_jugar.atacar(enemigo_de_enemigo)
     print(f"{enemigo_jugar} ataco a:{enemigo_de_enemigo} le bajo:{daño}")
     if enemigo_de_enemigo.vida <= 0:
        equipo_rival.remove(enemigo_de_enemigo)
        print("----------------------------------")
        print(f"MURIO:{enemigo_de_enemigo.nombre}")
        print("----------------------------------")
     if len(equipo_rival) <= 0:
          print("GANARON LOS ENEMIGOS")
          exit()
def turno_jugador(equipo_de_los_buenos, equipo_enemigo):
    if len(equipo_enemigo) <= 0:
         print("GANAMOS")
         exit()
    print("TU EQUIPO:")
    print("----------------------")
    for i in equipo_de_los_buenos:
        print(i)
        print(repr(i))
    print("----------------------")
    Personaje = input("eligue un personaje de tu equipo para atacar [solo el nombre]: ").lower()
    for i in equipo_de_los_buenos:
         if i.nombre == Personaje:
              if i.clase == "curandero":
                   curar = input("eligue un personaje de tus aliados para curar [solo el nombre]: ").lower()
                   for a in equipo_de_los_buenos:
                        if a.nombre == curar:
                             curacion = i.atacar(a)
                             print(f"{Personaje}: CURO A {a.nombre} lo curo un total de:{curacion}")
                             return
                        else:
                             pass
              else:
                   pass
    print("EQUIPO ENEMIGO:")
    print("----------------------")
    for i in equipo_enemigo:
        print(i)
        print(repr(i))
    print("----------------------")
    nombre_enemigo = input("eligue su nombre del enemigo al que quieres atacar: ").lower()
    for i in equipo_de_los_buenos:
         if i.nombre == Personaje:
              for e in equipo_enemigo:
                   if e.nombre == nombre_enemigo:
                        daño = i.atacar(e)
                        print(f"{i.nombre} ataco a {e.nombre} y le bajo un total de:{daño}")
                        if e.vida <= 0:
                             print(f"el enemigo:{e.nombre} MURIO")
                             equipo_enemigo.remove(e)
                        return
                
         else:
              pass
    if len(equipo_enemigo) <= 0:
         print("GANASTE")
         return
def combate(equipo):
    enemigos = eleccion_de_Personajes_enemigos()
    print("TU EQUIPO:")
    print("----------------------")
    for i in equipo:
        print(i)
        print(repr(i))
    print("----------------------")
    print("EQUIPO ENEMIGO:")
    print("----------------------")
    for i in enemigos:
        print(i)
        print(repr(i))
    print("----------------------")
    print("QUE EMPIECE EL COMBATE")
    while True:
         print("TU TURNO")
         turno_jugador(equipo,enemigos)
         print("TURNO DE LOS ENEMIGOS")
         turno_de_enemigos(equipo,enemigos)
combate(equipo)

        
     
