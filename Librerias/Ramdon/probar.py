from random import choice
import sys
class pepito:
    def __init__(self):
        self.piedra = "piedra"
        self.papel = "papel"
        self.tijera = "tijera"
pepe = pepito()
listas = ["piedra","papel", "tijera"]
user = input("elige piedra papel o tijera: ").lower()
if user in listas:
    pass
else:
    sys.exit()

resultado = choice(listas)
if resultado == "piedra":
    print(f"pepe a elegido:{pepe.piedra}")
    if user == "papel":
        print("ganaste a pepe")
    elif user == "piedra":
        print("empataste a pepe")
    else:
        print("gano pepe pepe")
elif resultado == "papel":
    print(f"pepe a elegido:{pepe.papel}")
    if user == "tijera":
        print("ganaste a pepe")
    elif user == "papel":
        print("empataste a pepe")
    else:
        print("perdiste con pepe")
elif resultado == "tijera":
    print(f"pepe a elegido:{pepe.tijera}")
    if user == "piedra":
        print("ganaste a pepe")
    elif user == "papel":
        print("gano pepe")
    else:
        print("empataste con pepe")