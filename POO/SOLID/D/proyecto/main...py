#📁 Archivo 3: main.py (La Central de Ensamble - RECEPTOR)
#Su única responsabilidad (S): Correr la pantalla interactiva while True
#Tu misión: Importa tus archivos. Aquí es donde se hace la magia de la
#D:Instancias el motor que quieras: motor_elegido = ReactorNuclear()
#Creas el traje inyectándole ese motor por las tuberías del paréntesis: mi_traje = Exoesqueleto(motor_elegido)
#Monta el menú para que el chofer digite la distancia a avanzar, captura los errores del raise con tu try/except visual
#y pinta la telemetría en la PowerShell de Windows [INDEX_3].
import conecion1
import conecion2
while True:
    chofer = input("que Motor eliges celdasolar o ReactorNuclear: ").lower()
    Motor: conecion1.CeldaSolar | conecion1.ReactorNuclear | None = None#el moto puede ser dos cosas si no es una es None
    if chofer == "celdasolar":
        Motor = conecion1.CeldaSolar()
        Traje = conecion2.Exoesqueleto(Motor)
        print("esqueleto elegido listo")
        break
    elif chofer == "reactornuclear":
        Motor = conecion1.ReactorNuclear()
        Traje = conecion2.Exoesqueleto(Motor)
        print("esqueleto elegido listo")
        break
    else:
        print("No elegido")
while True:
    chofer = input("[avansar] [salir] : ").lower().strip()
    if chofer == "avansar":
        try:
            pasos = int(input("di un numero de cuantos pasos quieres dar"))
        except ValueError as error:
            print(str(error))
            print("di un numero")
        else:
            aguila = Traje.avansar(pasos)
            print(aguila)
    elif chofer == "salir":
        break
    else:
        print("no se reconoce la opcion")