#Archivo 2: conexion2.py (La Fábrica de Artillería - HIJOS)
#Su única responsabilidad (S): Programar el comportamiento físico de las máquinas en la RAM sin pintar pantallas
#Tu misión: Importa el padre (from conexion1 import TorretaBase). Crea dos clases hijas reales:
#TorretaLaser: Inicia con self.bateria = 100 Su método disparar gasta 2 de batería por cada tiro en la ráfaga y devuelve el reporte
#en texto plano TorretaMisiles: Inicia con self.municion = 10 y un pin de seguridad oculto en el constructor self._pin = "7777"
#(para cumplir la S) Su método disparar debe recibir exactamente el mismo enchufe del padre (rafaga: int -> str) para cumplir la L
#Valida el pin por dentro en el silicio y descuenta 1 misil por tiro Si se quedan sin insumos, lanzan un raise ValueError.
import conecion1#damos el clave exacto del archivo conecion1
class TorretaLaser(conecion1.TorretaBase):#hacemos una clase hija que ereda de su padre que se encuentra en conecion1 damos la ruta
    def __init__(self):#abrimos el constructor
        self.bateria = 100#empieza con 100 de bateria
    def disparar(self, rafaga:int) -> str:#metodo disparar rafaga necesita si o si un int y deve devolver obligatoriamente un texto
        if self.bateria <= 0:
            raise ValueError("Sin bateria")
        if self.bateria < rafaga * 2:
            raise ValueError("demasiados disparos para bateria")
        self.bateria -= (rafaga * 2)#multiplicamos * 2 la rafaga para que sea igual a bateria si ay 2 disparos bateria gasta 4 *2= 4 - 4
        return "DISPARO LASER"
class validar:
    def __init__(self):
        self.municion = 10
        self._pin = "7777"
    def disparar(self, pin:int) -> str:
        if str(pin) == self._pin:
            self.municion -= 1
            return "PIN CORRECTO DAMOS UNA MUNICION"
        else:
            raise PermissionError("PIN INCORRECTO NO DAMOS MUNICION")