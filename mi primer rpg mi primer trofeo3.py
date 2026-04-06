print("estas atrapado resuelve el acertijo")
hp_boss = 10
hp_you = 5
bucle = True
while bucle:
    print("si tengo 8 dedos y maria tiene 9 juan tiene 2 cuantos dedos tienen todos juntos")# 19
    print("A = 15 ")
    print("B = 19")
    print("C = 16")
    opciones = input("segun el texto cual es la respuesta correcta")
    if opciones == "A":
        print("NO VUELVE DENUEVO HACIA EL INICIO JAJAJA")
        continue
    elif opciones == "B":
        bucle = False
        print("jaja si es ese pero el siguiente acertijo sera mas dificil JAJA")
        print("bien lograste sobrevivir al primer acertijo ahora te toca el segundo este es dificil ajjaja")
        print("1 2 3 4")
        print(" el 1 significa tu perdision pero posible llave")
        print("2 puede ser tu salvacion pero al final no ay una puerta")
        print("3 estas de acuerdo que aqui moriras")
        print("4 el 4 es un misterio")
    elif opciones == "C":
        print("NO perdiste vuelve al inicio JAJAJA")
        continue
    else:
        print("esa no es una opcion perdiste vuelve al inicio JAJAJA")
    opciones2 = int(input("elije el 1, 2, 3, 4 :"))
    if opciones2 == 1:
        print("1 aceptaste ir a la perdision la posible llave resulto ser tu ilusion mueres")
    elif opciones2 == 2:
        print("2 significa salvacion pero vas al final no encuentras nada el letrero te dijo que no uvo salvacion mueres")
    elif opciones2 == 3:
         print("entras aunque sabes que moriras pero una luz te dice que no la sicologia reversa entonces vez la puerta para el siguiente asertijo ganaste")
    print("vaya vaya mis acertijos no son nada para ti al parecer eso no importa el ultimo acertijo es que te matee")
    print("vez una espada volando hacia a ti la agarras")
    print("ahora te toca luchar")
    luchar_boss = int(input("luchas con el jefe que haces numero 1 atacar numero 2 defender numero 3 romper escudo"))
    if luchar_boss == 1:
             print("atacas el jefe esquiva tu ataque te agarra del cueyo y te da un golpe")
             print(f"te bajo vida tu vida:{hp_you - 2}")
             print("no importa te vuelves a levantar")
             print("el boss vuela hacia a ti que haces 1 atacar tambien 2 un escudo 3 romper escudo")
             print("antes de que elijas el jeve te mata")
    elif luchar_boss == 2:
             print("te defiendes activando escudo el boss te mira confuso te aplasta con su pie ya que es gigante")
             print(f"tu vida esta 1 tu vida:{hp_you - 4}")
             print("entras en panico huyes")
             print("el boss te mira huyendo te atrapa y te mata perdiste")
    elif luchar_boss == 3:
             print("haces un ataque que rompe escudo pero no le afecta al bosss")
             print("es turno del boss")
             print(f"te manda un cohete que te baja 2 de vida tu vida:{hp_you - 2}") 
             print("aunque te aiga echo un ataque brutal tu sigues de pie")
             print("vez que el jefe tenia un silbato")
             print("decides agarrarlo")
             print("el jefe se asusta y trata de quitartelo")
             print("pero tu lo tocas")
             print("se escucha pasos gigantes")
             print("y sale la mascota del jefe que es un anciano moustro")
             print("el anciano estava encerrado y al tocarlo lo liberaste el anciano sin pensarlo quiere matar al jefe")
             print("te alias con el anciano")
             vida_de_anciano = 5
             print(f"el anciano ataca al jefe y le bajo 3 de vida vida del jefe:{hp_boss - 3}")
             print("el jefe agarra al anciano y lo aplasta contra el suelo")
             print(f"vida de anciano:{vida_de_anciano - 3}")
             print("el anciano esta muy mal herido")
             apoyo = int(input("no puedes quedarte biendo como matan a tu aliado que haces 1 atacar 2 huir"))
             if apoyo == 1:
                 print("atacas al jefe")
                 print(f"logras hacerle daño vida del jefe{hp_boss - 2} ")
                 print("el jefe se puso molesto y se abalansa contra ti")
                 print(f"pero justo cuando te iva matar el anciano se levanta y atraviesa una espada en el pecho del jefe vida del jefe{hp_boss - 3}")
                 print("el jefe se enfurese y agarra al anciano y lo golpea repetitivamente matandolo")
                 print(f"vida del anciano:{vida_de_anciano - 2}")
                 print("te enfureses")
                 apoyo2 = int(input("te enfureses bastante quieres usar todo tu energia para matarlo pero acambio tu tambien moriras = 1 oh atacarlo = 2 "))
                 if apoyo2 == 1:
                     print("usas todo tu ataque para matar al jefe explotas en el los dos mueren pero almenos lo mataste y vengaste al anciano")
                     bucle = False
                     print("final meh")
                 elif apoyo2 == 2:
                     print("desides atacar con ira haces un ataque potente que le bajas mucha vida al jefe")
                     print(" el jefe vuela hacia a ti con un ataque que haces?")
                     apoyo3 = int(input("te asustas pero si no actuas moriras que haces pon 1 si atacas tambien 2 si te defiendes 3 si haces un ataque rompe escudos"))
                     if apoyo3 == 1:
                         print("atacas pero el jefe es mucho mas fuerte que terminas muriendo")
                     if apoyo3 == 2:
                         print("te defiendes el ataque del jefe rebota hacia el")
                         print(f"vida del jefe: {hp_boss - 1}")
                         print("el jefe esta a un toque decides perdonarlo o matarlo?")
                         matar_or_perdonar = int(input("que haces pon 1 si es matar 2 si es perdonar"))
                         if matar_or_perdonar == 1:
                             print("te abalansas hacia el jefe con tu espada")
                             print("el activa escudo")
                             desactivar_escudo = int(input("que haces pon 1 atadar 2 defenderte 3 romper escudo"))
                             if desactivar_escudo == 1:
                                 print("atacas pero tu ataque rebota con el escudo del jefe")
                                 print(f"tu vida:{hp_you - 3}")
                                 print("mueres")
                             elif desactivar_escudo == 2:
                                 print("desides defenderte pero el jefe reacciona rapido y rompe tu escudo")
                                 print(f"tu vida:{hp_you - 3}")
                                 print("mueres")
                             elif desactivar_escudo == 3:
                                 bucle = False
                                 print("desides hacer el ataque de desactivar escudo rompes el escudo del jefe")
                                 print(f"vida del jefe.{hp_boss - 1}")
                                 print("el jefe muere haces una tumba para el anciano y se habre una puerta")
                                 
                                 print("resulto ser la salida te vas  ganaste")
                                 print("final vengativo")
                             else:
                                 print("mueres el jefe te termina matando")
                         elif matar_or_perdonar == 2:
                             print("desides perdonar el jefe aprovecha que lo perdonaste")
                             print("deside matarte el jefe aprovechando que tienes poca vida")
                             print("te mueres")
                             bucle = False
                             print("final traicionero")
                         else:
                             print("el jefe aprovecha tu distraccion y te mata")
                             
             elif apoyo == 2:
                 print("huyes el jefe te ve huyendo asi que va por ti pero el anciano le atraviesa una espada en su pecho")
                 print("el jefe esta sangrando el anciano lo quiere matar ahorcando pero el jefe lo agarra primero")
                 deves_hacer_algo = int(input("vez al anciano a punto de morir que haces pon 1 si lo ayudas 2 si lo dejas"))
                 if deves_hacer_algo == 1:
                     print("lo ayudas y no desides ser un cobarde y los dos juntos terminan matando al jefe")
                     print(f"vida del jefe {hp_boss - 7}")
                     print("por fin lo mataron se habre una puerta resulta ser la salida tu y el anciano ganaron y excaparon")
                     bucle = False
                     print("final bueno")
                 elif deves_hacer_algo == 2:
                     print("estas asustado tanto que no decides ayudar a tu aliado y buscas desesperadamente una salida que no ay")
                     print("el jefe mata al anciano")
                     print(f"vida del anciano:{vida_de_anciano}")
                     print("el jefe termina con el anciano y se va directo a ti pero tu por tu cobardia y tu miedo te termina matando")
                     bucle = False
                     print("final malo")
                 else:
                     print("mueres")
             else:
                 print("mueres")
            
    elif opciones2 == 4:
        bucle = False
        print("el misterio resulto ser un acantilado sin fin no pierdes te encuentras con un anciano que te va a guiar")
        print("el anciano te dice que todo estara bien")
        print("te das cuenta que en realidad no ay salida desides escapar en un hueco")
        print("el anciano no te deja huir pues el quiere comerte no resulto ser un anciano")
        print("tienes 2 opciones luchar o huir")
        opciones_anciano = (int)(input("escribe 1 si es luchar 2 si es huir: "))
        if opciones_anciano == 1:
            print("luchas agarras una espada los dos luchan ahora entraste en una guerra")
            print("apretas 1 para atacar 2 para defenderte y 3 para romper el escudo del enemigo")
            opciones_lucha = int(input("que opcion elijes"))
            if opciones_lucha == 1:
                print("atacas al anciano")
                print("el anciano le bajaron 1 vida de las 5 que tiene tu tienes 3 de vida")
                salud = 3
                salud_de_anciano = 4
                print("anciano se puso furioso")
                opciones_lucha2 = int(input("vaya el anciano se puso furioso que haces 1 atacar 2 escudo o 3 romper escudo"))
                if opciones_lucha2 == 1:
                    print("atacas pero el anciano ignora tu ataque y te come")
                elif opciones_lucha2 == 2:
                    print("pones tu escudo")
                    print("el ataque del anciano rebota asia el")
                    print("genial venciste al anciano")
                    print("vez un hueco de luz")
                    print("resultdo ser la salida")
                    print("felisidades ganaste")
                    bucle = False
                    print("ganaste ")
                elif opciones_lucha2 ==2:
                    print("pones roomper escudo pero el anciano te mira confuso y te mata")
                else:
                    print("no haces nada y el anciano te come")
            elif opciones_lucha == 2:
                print("activas tu escudo el anciano te mira confuso pero abre su boca y te come perdiste")
            elif opciones_lucha == 3:
                print("haces un ataque rompe escudo el ataque esta diseñado solo para que si el anciano activa escudo pero anciano no activo escudo y te come")
            else:
                print("no haces nada el anciano te come")
        elif opciones_anciano ==2:
            print("huyes el anciano te mira confuso y te mata")
        else:
            print("no haces nada y te mata")
    else:
        print("te mueres porque si")

              
                



        