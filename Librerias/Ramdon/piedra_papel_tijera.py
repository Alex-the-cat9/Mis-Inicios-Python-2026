from random import choices
from sys import exit
from time import sleep
Reglas = {
    "piedra":"tijera",
    "papel":"piedra",
    "tijera":"papel"
}
opciones_validas = list(Reglas.keys())
user = input("elige piedra papel o tijera: ").lower()
if user not in opciones_validas:
    print("opcion no valida saliendo del juego....")
    exit()
print("...")
sleep(6)
pepe_jugar = choices(opciones_validas,weights=[40,30,25], k=1 )[0]
if user == pepe_jugar:
    print("empataron")
elif Reglas[user] == pepe_jugar:
    print("GANASTE  pepe perdio")
else:
    print("PERDISTE pepe gano")