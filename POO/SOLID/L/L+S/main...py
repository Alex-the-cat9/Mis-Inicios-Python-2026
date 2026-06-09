#📁 Archivo 3: main.py (El Centro de Control Visual - RECEPTOR)
#Su única responsabilidad (S): Correr la pantalla interactiva while True.Tu misión:
#Importa tus clases de conexion2.py. Crea una lista llamada bateria_defensa: list[TorretaBase].
#Monta las opciones para que el chofer elija qué torreta disparar. El código del main debe meterle corriente a la torreta elegida
#usando exactamente la misma línea horizontal pasándole un solo entero: torreta.disparar(cantidad). 
#Captura los errores del raise con tu try/except visual para que la PowerShell no se caiga.
import conecion2
bateria_defensa: list[conecion2.conecion1.TorretaBase] = [conecion2.TorretaLaser()]
while True:
    chofer = input("[salir] [disparar]: ").lower()
    if chofer == "disparar":
        try:
            pin = int(input("di el pin: "))
            aguila2 = conecion2.TorretaLaser()
            aguila = conecion2.validar()
            poderoso = aguila.disparar(pin)
            print(poderoso)
            cantidad = int(input("di la cantidad solo numeros: "))
            disparo = aguila2.disparar(cantidad)
            print(disparo)
        except Exception as error:
            print(str(error))
    elif chofer == "salir":
        break
    else:
        print("no se reconoce")
