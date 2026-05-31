#🚨 EL EXPEDIENTE DEL RETO: TanqueGuerra ⚔️🛡️
#Tu misión es inyectar un TanqueGuerra en el sistema  Aquí tienes sus especificaciones genéticas
#para la RAM [INDEX_3]:Gasto de Energía: Consume 5 de energía por cada kilómetro recorrido (es un vehículo pesado)
#Su contador de kilómetros debe llamarse exactamente kilometros
#(con la 's' al final, igual que el submarino) Si se queda sin combustible, debe disparar el mismo raise ValueError("energia agotada")
#🥷 LAS REGLAS MARCIALES DEL DESPLIEGUE (La trampa de la O)Para que tu victoria sea legítima ante los ingenieros de Silicon Valley
#debes cumplir estas dos restricciones de hardware [INDEX_3]:¡ESTRICTAMENTE PROHIBIDO MODIFICAR TU CÓDIGO VIEJO! No puedes abrir
#tu archivo modelo.py a meterle mano al submarino ni a la nave  No puedes alterar los cimientos del plano de hierro que ya funciona
#LA EXPANSIÓN MEDIANTE FIBRA ÓPTICA (La O a nivel de archivos): Vas a crear un ARCHIVO TOTALMENTE NUEVO llamado pesado.py
#al lado de tus otros scripts  Ahí adentro vas a importar a tu padre abstracto escribiendo from modelo import vehiculo
#Adentro de ese archivo nuevo, vas a programar tu clase TanqueGuerra heredando del padre 🔌
#Cómo lo conectas en tu interfaz main.py:En tu archivo visual, lo único que tienes permitido hacer es importar
#tu nueva clase al inicio (from pesado import TanqueGuerra), instanciarlo abajo (Tanque = TanqueGuerra())
#y agregar la opción [tanque] adentro de tu compuerta de selección de viaje  Tu bucle interactivo y tus funciones de garaje.py
#se quedan 100% CERRADAS a modificaciones internas; solo consumen el nuevo cable
import OCP
class Tanque_de_guerra(OCP.vehiculo):
    def __init__(self):
        self.metros = 0
        self.kilometros = 0
        self.polvora = 1000
        self.combustible = 1000
    def viajar(self,distancia):
        if self.combustible <= 0:
            raise ValueError("sim combustible")
        while distancia >= 100:
            self.kilometros +=1
            distancia -= 100
            self.combustible -= 5
        self.metros += distancia
        while self.metros >= 100:
            self.kilometros +=1
            self.metros -= 100
            self.combustible -=5
    def disparar(self, disparo):
        if self.polvora <= 0:
            raise ValueError("se nos acabo la polvora")
        if disparo < 100:
            print("se gasto polvora porque no pusimos suficiente para un disparo")
        else:
            print("DISPAROOO")
        self.polvora -= disparo
Tanque = Tanque_de_guerra()
while True:
    user = input("quieres viajar o disparar o salir: ").lower()
    if user == "salir":
        break
    elif user == "viajar":
        try:
            distancia = int(input("diga la distancia que quiere viajar solo numeros: "))
            Tanque.viajar(distancia)
        except ValueError as error:
            if str(error) == "sim combustible":
                print("se quedo sin combustible señor")
            else:
                print("no deve escribir letras para la distancia solo numeros")
    elif user == "disparar":
        try:
            polvora = int(input("diga la cantidad de polvora que quiere meter al cañon: "))
            Tanque.disparar(polvora)
        except ValueError as error:
            if str(error) == "se nos acabo la polvora":
                print(str(error))
            else:
                print("escribio letras en la cantidad")
    else:
        print("no reconocido")

        
    
