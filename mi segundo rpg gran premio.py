mochila = ["antorcha"]
print("eres un aventurero en estas ruinas")
while True:
    print("caminas y te encuentras con un objeto misterioso")
    espada = str(input("parece ser algo filoso y largo como un machete pero no es machete: "))
    if espada == "espada":
        print("eso es cierto es una espada añadido a nuestra mochila")
        mochila.append(espada)
        print(f"tu mochila:{mochila}")
        break
    else:
        print(f"no parece ser una:{espada} intentemos denuevo")
        continue
print("muy bien aventurero sigamos con  la aventura")
print("un monton de pasto esta bloqueando tu camino aventurero que usas de tu mochila")
while True:
    opciones = str(input(f"en tu mochila tienes:{mochila} que usas para ese pasto: "))
    if opciones == "antorcha":
        print("la antorcha no esta encendida con fuego aventurero")
    elif opciones == "espada":
        print("muy bien aventurero usaste la espada para eliminar el pasto")
        print("pero a causa de eso tu espada se gasto se elimina de tu mochila pero tu aventura sigue")
        mochila.pop()
        print(f"tu mochila:{mochila}")
        break
    else:
        print("alto ai aventurero esa no es una opcion")
print("solo tienes un objeto aventurero sigues caminando y te encuentras con fuego")
antocha_prendida = "antorcha con fuego" 
while True:
    opciones = str(input("decides prender tu antorcha de fuego aventurero? diga si o no: "))
    if opciones == "si":
       print("bien aventurero su antorcha esta encendida")
       mochila.pop()
       mochila.append(antocha_prendida)
       print(f"su inventario:{mochila}")
       break
    if opciones == "no":
        
        print("wow bueno aventurero respeto sus decisiones sigamos con la aventura")

        print("aventurero losiento decirte pero nos encontramos con una pared de madera que arriba dice ser la salida")
        print("no tenemos nada para quemar esa madera perdimos")
        continue 
    else:
        print("aventurero esa no es una opcion..")
print("estas caminando y te encuentras con algo..")
print("es la salida aventurero pero esta cubierta con madera")
print("decidiste quemarlo la madera y por fin saliste")
mochila.pop()
print("ganaste aventurero")
print(f"tu mochila tiene:{len(mochila)} objetos y son {mochila}")