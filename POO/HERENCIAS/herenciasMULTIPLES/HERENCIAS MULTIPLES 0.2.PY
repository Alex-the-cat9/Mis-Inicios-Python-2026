#maestro.IA:El Reto: Crea una clase Auto (con velocidad) y una clase Avión (con altitud) [INDEX_3]. Luego diseña la clase hija AutoVolador
#que herede de ambos usando Auto.__init__(self, ...) y Avion.__init__(self, ...) [INDEX_34].
class auto:
    def __init__(self, velocidad):
        self.velocidad = velocidad
class avion:
    def __init__(self, altitud):
        self.altitud = altitud
class autovolador(auto, avion):
    def __init__(self):
        velocida = int(input("usuario compro un auto diga la velocidad que deceee tener solo numero: "))
        if velocida > 30:
            print("tu auto sera muy veloz te encanta la velocidad")
        altitu = int(input("bien bien ahora diga la altitud que decea tener de su auto volador: "))
        if altitu > 30:
            print("wow le gusta volar por los cielos")
        print("comprado que tenga un buen dia")
        auto.__init__(self,velocida)
        avion.__init__(self,altitu)
    def mostra(self):
        print("SU AUTO:")
        print(f"VELOCIDAD:{self.velocidad}")
        print(f"ALTURA:{self.altitud}")
usuario = input("desea comprar un auto volador? [si] [no]: ").lower()
if usuario == "si":
    try:
     primer_auto = autovolador()
    except ValueError:
        print("le dijimos solo numeros....")
    else:
        primer_auto.mostra()
        print("listo que tenga un buen dia adios")

else:
    print("bueno siguiente")
#📋 El Nuevo Reto Simplificado Tu misión:crear el CortafuegosInteligente combinando dos padres, pero esta vez el segundo padre tendrá
#un superpoder 100% de texto plano que entenderás al milisegundo [INDEX_3].
#Padre 1 (FiltroTrafico): Revisa si la IP es segura [INDEX_3].
#Padre 2 (MensajeOculto): Su único trabajo es recibir un mensaje y, si la llave secreta es la correcta, te cambia el texto
#por la palabra "ACCESO_PERMITIDO" [INDEX_3]. ¡Pura lógica de strings! [INDEX_3]
#Hijo (CortafuegosInteligente): Hereda de ambos, pide los datos con input()
#y distribuye el ADN con el punto y el self (FiltroTrafico.__init__(self, ...) y MensajeOculto.__init__(self, ...))
#[INDEX_34, INDEX_37].
class FiltroTrafico:
    def __init__(self, IP):
        self.IP = str(IP)
    def analizar_ip(self):
        if "192.168" in self.IP:
            print(f"IP:{self.IP} es 100% segura")
        else:
            print(f"IP:{self.IP} IP sospechosa Peligro")
class MensajeOculto:
    def __init__(self, llave_seguridad):
        self.llave_seguridad = llave_seguridad
    def verificar(self):
        if self.llave_seguridad == 60:
            print("Datos del servidor ACCESO TOTAL permitido")
        else:
            print("datos negados")
class CortafuegosInteligente(FiltroTrafico, MensajeOculto):
    def __init__(self):
        ip = input("ingrese su dirrecion de IP: ").strip()
        llave = int(input("configure su llave secreta: "))
        super().__init__(ip)
        MensajeOculto.__init__(self,llave)
try:
    hacke = CortafuegosInteligente()
    hacke.analizar_ip()
    hacke.verificar()
except ValueError:
    print("ERROR escribiste una letra en la llave de seguridad")
