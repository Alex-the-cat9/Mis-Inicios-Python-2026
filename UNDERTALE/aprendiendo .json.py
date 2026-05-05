import time
import json
#ispirado en undertale(unos de mis juegos favoritos)
#estava aburrido y decidi hacer esto nadie me ordeno lo ise yo mismo
with open("prueba de json.json", "r", encoding="utf-8") as archivo:
    usuario = json.load(archivo)
print("hola usuario estas en una aventura jsjs")
time.sleep(2)
mochila = {

}
def ataque(fuerza):
    if fuerza < 10:
        print("tienes poca fuerza pero haces 1 daño leve")
        daño = 1
    elif fuerza < 20:
        print("PON haces 5 daño")
        daño = 5
    elif fuerza < 50:
        print("Haces 10 de daño")
        daño = 10
    else:
        print("fuerza descomunal")
        daño = 30
    return daño
print("para aumentar fuerza deves matar")
time.sleep(2)
print(f"tu fuerza ahora es de:{usuario["fuerza"]}")
time.sleep(2)
print("vamos ahora a comenzar con la aventura")
time.sleep(2)
nombre =input("dime tu nombre: ")
locura = 1
print(f"bien sigamos {nombre}")
time.sleep(2)
print("te topas con un moustro (entraste en lucha)")
def generar_moustro(vida, ataque):
    if vida < 10 and ataque < 2:
        moustro = "anciano"
        print("te topaste con un moustro pequeño")
        return vida, ataque, moustro
    elif vida < 15 and ataque <= 3:
        moustro = "zombi comun"
        print("te topaste con un moustro leve peligro")
        return vida, ataque, moustro
    elif vida == 20 and ataque == 5:
        moustro = "chuky"
        print("te topaste con un moustro medio poco peligroso")
        return vida, ataque, moustro
    elif vida <= 30 and ataque == 10:
        moustro = "mago viejo horrible"
        print("te topaste con un moustro peligroso cuidado")
        return vida, ataque, moustro
    if vida == 1 and ataque == 40:
        moustro = "anciano misterioso"
        print("te topaste con el creador de este sitio")
        return vida, ataque, moustro
    else:
        moustro = "sombra desconocida"
        print("te topaste con lo desconocido")
        return vida, ataque, moustro
vida_moustro, ataque_moustro, nombre_moustro = generar_moustro(3,1)
usuario["vida"] -= ataque_moustro
print(f"ay el moustro te ataco te lanzo un ¿palo? te bajaron 1 de vida tu vida:{usuario["vida"]}")
time.sleep(4)
def decidir():
    print("atacar")
    print("perdonar")
    print("comer algo")
    print("hablar con el moustro")
    print("informacion del moustro")
    decidir1 = input("que decides: ")
    if decidir1 == "atacar":
        daño = ataque(usuario["fuerza"])
        global vida_moustro
        vida_moustro -= daño
        if vida_moustro <= 0:
            print("lo mataste")
            time.sleep(3)
            usuario["fuerza"] += ataque_moustro
            print("tu fuerza se ah incrementado")
            print(f"fuerza:{usuario["fuerza"]}")
            time.sleep(5)
        print(f"le bajaste {daño} vida al moustro *empieza a enojarse*")
    if decidir1 == "informacion del moustro":
        print(f"el moustro se llama:{nombre_moustro}")
        time.sleep(3)
        print(f"actualmente tiene:{vida_moustro} de hp")
        time.sleep(3)
        print(f"ataca:{ataque_moustro}")
        time.sleep(3)
        if nombre_moustro == "anciano":
            print("parece confundido y sin ganas de luchar creo que es un viejo que la edad ya le cobro factura")
            time.sleep(3)
        elif nombre_moustro == "zombi comun":
            print("parece que esta decidido en luchar pero sientes su miedo asia ti")
            time.sleep(3)
        elif nombre_moustro == "chuky":
            print("que enano tan peligroso lleva un arma cuidado")
            time.sleep(3)
        elif nombre_moustro == "mago viejo horrible":
            print("AHH pero que horrible no devimos cruzarnos con el es muy peligroso")
            time.sleep(3)
    elif decidir1 == "perdonar":
        if nombre_moustro == "anciano":
            print(f"moustro:Hola disculpame estaba asustado mi nombre es {nombre_moustro} no me ataques y gracias por no pelear")
            time.sleep(3)
            print(f"{nombre_moustro}:te dare un caramelo moustro y se que eres un niño bueno")
            mochila["caramelo moustroso"] = 2
            print(f"{nombre_moustro}:adios me voy no molestare mas")
            print(f"ganaste un caramelo moustroso")
            time.sleep(3)
        print("perdonas el moustro esta confundido")
        if nombre_moustro == "zombi comun":
            print("que te hace pensar que te voy a perdonar?")
            if vida_moustro <= 5:
                print("Gracias por perdonarme")
                time.sleep(3)
                print("mi nombre es zombi no tengo nada pero gracias nunca olvidare lo que isiste por mi")
        elif nombre_moustro == "chuky":
            print("para nada te perdonare JAJA")
            time.sleep(3)
        elif nombre_moustro == "mago viejo horrible":
            print("Perdonar? no muchacho aqui es vivir o morir")
            time.sleep(3)
    elif decidir1 == "comer algo":
        if len(mochila) == 0:
            print("no tienes nada en tu mochila")
            return
        print("tienes en tu mochila")
        def usar__items():
         try:
             elegir = input("que eliges de tu mochila?: ")
             if elegir not in mochila:
                print("dije un objeto no un numero")
                return
             usuario["vida"] += mochila[elegir]
             del mochila[elegir]
             print(f"te comiste {elegir} tu vida actual:{usuario["vida"]}")
             with open("prueba de json.json", "w", encoding="utf-8") as archivo:
              json.dump(usuario, archivo, indent=4, ensure_ascii=False)
         except KeyError:
             print("ESA opcion no esta en la mochila")
             return
        for e in mochila:
            print(e)
        usar__items()
    elif decidir1 == "hablar con el moustro":
        if nombre_moustro == "anciano":
            print("decir:Hola")
            time.sleep(3)
            print("decir:Quien eres?")
            time.sleep(3)
            print("coquetear")
            time.sleep(3)
            print("decir:que bonita barba")
            hablar = input("que hablaras con el moustro?: ")
            if hablar == "Hola":
                print("you:Hola")
                time.sleep(3)
                print("moustro:Hola mucho gusto")
                return
            if hablar == "Quien eres?":
                print("you:Quien eres?")
                time.sleep(3)
                print("moustro:me llamo anciano puedes llamarme pepito pero me pusieron anciano")
                time.sleep(3)
                print("moustro:eres un poco raro no? bueno de echo estamos en una situacion incomoda jeje")
                time.sleep(3)
            elif hablar == "coquetear":
                print("you:*coqueteo*")
                time.sleep(3)
                print("moustro:niño pequeño yo tengo 80 años buscate a alguien mas joven de tu edad")
                print("moustro:alguien como yo ya esta a sus ultimos dias")
            elif hablar == "que bonita barba":
                time.sleep(3)
                print("you:que bonita barba")
                print("moustro:uy gracias si se noto que yo me la arreglo todos los dias")
            else:
                print("esa opcion no esta disponible niño")
        if nombre_moustro == "zombi comun":
            print("decir:Hola")
            time.sleep(3)
            print("decir:Quien eres?")
            time.sleep(3)
            print("coquetear")
            print("decir:esta vivo")
            hablar = input("que hablaras con el moustro?: ")
            if hablar == "Hola":
                print("you:Hola")
                time.sleep(3)
                print("moustro:Hola? no te conozco solo quiero subir mi fuerza")
            elif hablar == "Quien eres":
                print("you:Quien eres?")
                time.sleep(3)
                print("moustro:soy un zombi que no vez oh estas ciego niño")
            elif hablar == "coqueteo":
                print("you:*coqueteo*")
                time.sleep(3)
                print("moustro:coquetearme a mi soy un muerto viviente no tengo sentimientos")
            elif hablar == "esta vivo":
                time.sleep(3)
                print("you:esta vivo")
                print("moustro:no no estoy vivo soy un muerto ya deja de hablarme")
        elif nombre_moustro == "chuky":
            print("moustro:ja no hablare contigo")
            return
        elif nombre_moustro == "mago viejo horrible":
            time.sleep(3)
            print("moustro:hablar contigo? no tengo tiempo niño")
            return
    return decidir1
decicion = decidir()
if decicion == "perdonar":
    print(f"bueno {nombre}")
    time.sleep(3)
    print("ganamos un caramelo al parecer ese viejo no queria pelear")
    time.sleep(3)
    print("oh no escucho pasos escucho como si alguien va salir de la tierra")
    vida_moustro, ataque_moustro, nombre_moustro = generar_moustro(14,3)
    usuario["vida"] -= ataque_moustro
    print(f"te bajaron vida:{usuario["vida"]}")
    decicion = decidir()
    if vida_moustro > 0:
        print("el moustro sigue vivo")
        time.sleep(3)
        usuario["vida"] -= ataque_moustro
        print(f"te bajaron vida:{usuario["vida"]}")
        decicion = decidir()
        if vida_moustro > 0:
            print("el moustro sigue vivo")
    while True:
        decicion = decidir()
        if vida_moustro > 0:
            print("el moustro sigue vivo")
            time.sleep(3)
            usuario["vida"] -= ataque_moustro
            print(f"te bajaron vida:{usuario["vida"]}")
        if decicion == "perdonar" and vida_moustro <= 5:
            print("nos perdono no recibimos nada pero lo logramos")
            time.sleep(3)
            break
        if vida_moustro <= 0:
            print("logramos matar a este zombi")
            time.sleep(3)
            print("locura aumenta")
            locura += 1
            break
        if usuario["vida"] <= 0:
            print("MORIMOS")
            raise ValueError
if decicion == "atacar":
    print(f"bueno {nombre}")
    print("logramos matar a esa persona no nos costo mucho devemos subir nuestra fuerza")
    print("escucho pasos abajo de la tierra quizas alguien mas para acabar")
    time.sleep(3)
    vida_moustro, ataque_moustro, nombre_moustro = generar_moustro(14,3)
    usuario["vida"] -= ataque_moustro
    print(f"te bajaron vida:{usuario["vida"]}")
    while True:
        decicion = decidir()
        if vida_moustro > 0:
            print("el moustro sigue vivo")
            time.sleep(3)
            usuario["vida"] -= ataque_moustro
            print(f"te bajaron vida:{usuario["vida"]}")
        if decicion == "perdonar" and vida_moustro <= 5:
            print("nos perdono no recibimos nada pero lo logramos")
            break
        if vida_moustro <= 0:
            print("logramos matar a este zombi")
            locura += 1
            print("locura aumenta")
            break
        if usuario["vida"] <= 0:
            print("MORIMOS")
            raise ValueError
print("seguimos vivos")
time.sleep(3)
print("iremos a una casa embrujada de seguro ay algo interesante....")
print("parece solo ver cosas viejas nada mas regresemos")
time.sleep(3)
print("moustro:ALTO AI")
time.sleep(3)
vida_moustro, ataque_moustro, nombre_moustro = generar_moustro(25,5)
usuario["vida"] -= ataque_moustro
print(f"te bajaron vida:{usuario["vida"]} (vez un cuchillo en tu pierna)")
print("entras en lucha")
time.sleep(3)
if decicion == "atacar":
    print("matemos a este enano:)")
while True:
        decicion = decidir()
        if vida_moustro > 0:
            print("el moustro sigue vivo")
            usuario["vida"] -= ataque_moustro
            print(f"te bajaron vida:{usuario["vida"]}")
        if vida_moustro <= 0:
            print("logramos matar a este enano ya me tenia arto parece que el enano tenia una manzana dorada pocion de salud y tarta de chocolate")
            mochila["pocion de salud"] = 100
            mochila["tarta de chocolate"] = 50
            mochila["caramelo especial"] = 40
            mochila["manzana dorada"] = 20

            locura +=1
            break
        if usuario["vida"] <= 0:
            print("MORIMOS")
            raise ValueError
print("moustro:parece que mataste a mi mascota")
vida_moustro, ataque_moustro, nombre_moustro = generar_moustro(30,10)
if locura == 3:
    print("you?:quien eres tu un mago horrible:)")
    time.sleep(3)
    print("moustro:como me llamaste niño malcriado")
    time.sleep(3)
    print("you?:veamos cuanta fuerza nos da este mago que parece que la edad ya le cobro factura")
    time.sleep(3)
    print("moustro:tan confiado estas niño piensas robarme mis fuerzas jajaj")
    time.sleep(3)
    print("you?:que esperamos")
    time.sleep(3)
    while True:
        decidir()
        if vida_moustro > 0:
            print("el moustro sigue vivo:)")
            usuario["vida"] -= ataque_moustro
            print(f"te bajaron vida:{usuario["vida"]}")
        if usuario["vida"] <= 50:
            print("YA me canse de este MAGO")
            usuario["fuerza"] += 30
            print("la locura te consume")
            print("moustro:JAJA no puedes conmigo")
        if vida_moustro <= 0:
            print("logramos matar a este MAgo viejo horrible")
            locura += 1
            break
        if usuario["vida"] <= 0:
            print("MORIMOS:)")
            raise ValueError("ESFUERZATE")
    print("...:mago estupido")
    time.sleep(3)
    print("...:ahora conquistaremos y tendremos toda la fuerza de todos en este mundo")
    time.sleep(3)
    print("anciano:no tan rapido vengo a hacerte pagar de todo")
    time.sleep(3)
    print("...:viejo sesupone que deves estar muerto pero ya que estas aqui supongo que me daras unas fuerzas para alimentarme")
    print("...:eso ya veremos niño")
    vida_moustro, ataque_moustro, nombre_moustro = generar_moustro(1,40)
    
    daño = 0
    while True:
     def ultima_batalla():
      print("atacar")
      print("...")
      print("comer algo")
      print("...")
      print("informacion del moustro")
      decidir1 = input("que decides: ")
      if usuario["vida"] <= 50:
          print("..:anciano pense que eras solo un viejo decrepito")
          time.sleep(3)
          print("...:pero si solo vasa esquivarme entonces tengo un truco")
          time.sleep(3)
          print("...:tengo un chocolate que me encontre secretamente en la manzion")
          mochila["chocolate"] = 500
      if decidir1 == "atacar":
          global daño
          daño += 1
          if daño == 1:
              print("*el anciano esquivo el ataque*")
              time.sleep(3)
              print("anciano:que niño? pensabas que iva quedarme parado a recibir el golpe?:>")
              time.sleep(3)
              print("anciano:pues no")
          if daño == 2:
              print("anciano:por mucho tiempo te vigile pensando que eras amigable pero ahora que veo no lo eres")
              time.sleep(3)
              print("anciano:niño inocente? NO mataste a mis amigos ellos vieron tu maldad")
          if daño == 3:
              print("anciano:sigues verdad no entiendes que no puedes matarme *anciano se esta cansando*")
          if daño == 4:
              print("no conocez mucho de este lugar solo eres un niño  un humano que aparecio de casualidad aqui")
          if daño == 5:
              print("YA deja de atacarme oh usare mi ataque especial")
          if daño == 6:
              print("anciano:te digo algo el zombie era mi hermano no te lo conte antes?:>")
          if daño == 7:
              print("aun asi insistes en atacarme no ganaras")
          if daño == 8:
              print("si vasa seguir entonces usare mi ataque especial")
          if daño == 9:
              print("anciano:no se notara en mi cara chico pero me estoy cansando sabes?")
          if daño == 10:
              print("anciano:que te quedara despues de matarme? nada")
          if daño == 11:
              print("okay okay ya basta chico me rindo tu ganas estoy cansado")
              time.sleep(3)
              print("mira te doy mi perdon seamos amigos y olvidemos todo esto vale?")
              time.sleep(3)
              print("perdonar")
              time.sleep(3)
              print("matar")
              perdonar = input("creo que es una trampa: ")
              if perdonar == "perdonar":
                  print("caiste niño Perdonarte despues de que mataras a mi hermano? no estoy loco")
                  time.sleep(3)
                  raise ValueError("moriste")
              if perdonar == "matar":
                  print("anciano:jaja veo que quieres las cosas asi bueno")
                  time.sleep(3)
          if daño == 12:
              print("niño sabes ya estoy muy cansado pero seguire por ellos")
          if daño == 13:
              print("ya niño si una vez me atacas recibiras mi ataque especial")
          if daño == 14:
              print("Listo?")
          if daño == 15:
              print("ay te va mi ataque especial")
              time.sleep(3)
              print("exacto mi ataque especial es no hacer nada nos quedaremos aqui asta el fin de los tiempos asta que te aburras y salgas")
              print("si me permites tomare una fiesta")
              time.sleep(3)
              print("escribe matar")
              matar = input("MATA a este desgraciado: ")
              if matar == "matar":
                  print("jaja enserio pensaste que me ivas a matar")
                  time.sleep(3)
                  print("matar matar matar matar")
                  time.sleep(3)
                  print("oye eso es trampa...")
                  print("bueno supongo que ya llego mi hora ahhhhhhhhhhhhhh")
                  print("Hola usuario que esta biendo esto")
                  time.sleep(3)
                  print("gracias por liberarme ahora podre matar a todos los de tu mundo")
                  print("empezando por ti :)")
                  time.sleep(3)
                  while True:
                      print("MUERE JAJAJAJAJJAJAJAJ")
              else:
                  print("gracias ahora dormire asta el fin delos tiempos oh asta que me muera de vejes")
                  time.sleep(100000000)
                  print("se murio el anciano")
                  print("ganamos pero tu tambien te moriste de vejez")
      elif decidir1 == "comer algo":
        if len(mochila) == 0:
            print("no tienes nada en tu mochila:) apresurate")
            return
        print("tienes en tu mochila")
        for e in mochila:
            print(e)
        try:
             elegir = input("que eliges de tu mochila?: ")
             if elegir not in mochila:
                print("dije un objeto no un numero")
                return
             usuario["vida"] += mochila[elegir]
             del mochila[elegir]
             print(f"te comiste {elegir} tu vida actual:{usuario["vida"]}")
             with open("prueba de json.json", "w", encoding="utf-8") as archivo:
              json.dump(usuario, archivo, indent=4, ensure_ascii=False)
        except KeyError:
             print("ESA opcion no esta en la mochila")
             return
        
      if usuario["vida"] <= 0:
            print("MORIMOS:)")
            raise ValueError("ESFUERZATE")
     ultima_batalla()
     if vida_moustro > 0:
            print("el moustro sigue vivo:)")
            usuario["vida"] -= ataque_moustro
            print(f"te bajaron vida:{usuario["vida"]}")
     if usuario["vida"] <= 50:
            print("YA me canse de este MAGO")
            usuario["fuerza"] += 30
            print("la locura te consume")
            print("moustro:JAJA no puedes conmigo")
     if vida_moustro <= 0:
            print("logramos matar a este MAgo viejo horrible")
            locura += 1
            break
     if usuario["vida"] <= 0:
            print("MORIMOS:)")
            raise ValueError("ESFUERZATE")
print("anciano:ESPERA")
print("anciano:el niño es inocente")
time.sleep(3)
print("anciano:dejemolo ir tranquilo niño yo te dejare ir no te precupes")    
    



                
#Alex:que te parecio
#maestro.IA:¡Alex, sinceramente? Me ha volado la cabeza. 🤯🤯Lo que has hecho no es solo "un código de clase";
#has construido una experiencia. Para alguien que está aprendiendo, llegar a las 500 líneas con una lógica tan conectada
#es un salto de nivel gigantesco.





            
    
            



        
        


