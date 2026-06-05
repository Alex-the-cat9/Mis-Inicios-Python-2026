#🏛️ EL PLANO DE INGENIERÍA:
#Tus 3 Capas de CiberdefensaVas a crear una carpeta llamada FlotaSOLID en tu VS Code
#vas a soldar exactamente 3 archivos independientes, siguiendo estrictamente la ley del nombre y del contrato:📁 Archivo 1:
#modelo.py (La Bóveda del Contrato - CERRADA)Su nombre dice:
#Contener la genética pura Tu misión: Escribe la clase abstracta Vehiculo(abc.ABC) con su @abc.abstractmethod
#def viajar(self, distancia): [INDEX_3].La Expansión Abierta:
#Abajo de ella, hereda y crea dos clases hijas reales: NaveEspacial y Submarino
#Cada una debe iniciar con una variable de energía (self.energia = 100) y una de posición
#(self.coordenada = 0) Al viajar(), la Nave gasta 2 de energía por cada kilómetro;
#el Submarino gasta 1 de energía [INDEX_3]. Si se quedan sin energía, lanzan un
#raise ValueError("Energia agotada") [INDEX_3]. ¡Prohibido usar print() aquí [INDEX_3]!
import abc
class vehiculo(abc.ABC):
    @abc.abstractmethod
    def viajar(self, distancia):
        pass
class NaveEspacial(vehiculo):
    def __init__(self):
        self.energia = 100
        self.kilometro = 0
        self.metros = 0
        self.energia_minima = 0
    def viajar(self, distancia):
        if self.energia <= 0:
            raise ValueError("energia agotada")
        while distancia >= 100:
            distancia -= 100
            self.kilometro +=1
            self.energia -=2
        if distancia < 100:
            if distancia <0:
                pass
            else:
                self.metros += distancia
                self.energia_minima += distancia
        while self.metros >= 100:
            self.kilometro += 1
            self.metros -= 100
        while self.energia_minima >= 100:
            self.energia -= 2
            self.energia_minima -= 100
class Submarino(vehiculo):
    def __init__(self):
        self.energia = 100
        self.kilometros = 0
        self.metros = 0
        self.energia_minima = 0
    def viajar(self, distancia):
        if self.energia <= 0:
            raise ValueError("energia agotada")
        while distancia >= 100:
            distancia -= 100
            self.kilometros +=1
            self.energia -=2
        if distancia < 100:
            if distancia <0:
                pass
            else:
                self.metros += distancia
                self.energia_minima += distancia
        while self.metros >= 100:
            self.kilometros += 1
            self.metros -= 100
        while self.energia_minima >= 100:
            self.energia -= 2
            self.energia_minima -= 100
