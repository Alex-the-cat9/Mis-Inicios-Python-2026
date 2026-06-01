from mochila import Personajes, Personajes_fusionados, agregar_guerrero, procesar_fusion
if __name__ == "__main__":
    while True:
        user = input("[agregar] [fusionar] [ver] [salir]: ").lower().strip()
        if user == "agregar":
            try:
                nombre = input("di el nombre del guerrero: ")
                poder = int(input("di el poder que va tener solo numeros: "))
            except ValueError:
                print("eran solo numeros.....")
            else:
                agregar_guerrero(nombre, poder)
        elif user == "fusionar":
            for e,i in Personajes.items():
                print(e)
            numero1 = input("elige uno de los Personajes: ")
            numero2 = input("elige al segundo personaje: ")
            if numero1 in Personajes and numero2 in Personajes:
                Personaje_fusionado = procesar_fusion(numero1, numero2)
                if Personaje_fusionado == "mochila vacia":
                    print("ERROR AL FUCIONAR MOCHILA VACIA O SOLO TIENES 1 PERSONAJE")
                else:
                    print("FUSION EXITOSA")
                    print(Personaje_fusionado)
                    print("----------------")
        elif user == "ver":
            print("Personajes NO fusionados:")
            for e,i in Personajes.items():
                print(e)
            print("Personajes FUSIONADOS:")
            for e,i in Personajes_fusionados.items():
                print(e)
            print("--------------------")
        elif user == "salir":
            print("gracias por jugar")
            break
        else:
            print("opcion incorrecta")