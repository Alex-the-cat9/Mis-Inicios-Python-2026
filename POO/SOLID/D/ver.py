#Crea el Contrato (Abstracción): Define una clase base abstracta llamada Vehiculo.
#Dentro de ella, declara un método vacío llamado acelerar usando el decorador que obliga a implementarlo.
#Adapta los Vehículos (Bajo Nivel): Haz que la clase AutoDeCarreras herede de tu nueva clase Vehiculo.
#Crea también una clase Moto que herede de Vehiculo. Asegúrate de que ambas escriban su propia versión del método acelerar.
#Libera al Piloto (Alto Nivel): Modifica la clase Piloto. Quita la línea donde creas el auto fijo.
#Ahora, haz que el método __init__ reciba el vehículo como un parámetro desde afuera y guárdalo en self.vehiculo.
#Haz la Prueba: Afuera de las clases, crea un objeto moto y un objeto auto. Luego, crea un piloto pasándole la moto, y hazlo conducir.
import abc
class Vehiculo(abc.ABC):
    @abc.abstractmethod
    def acelerar(self):
        pass
class AutoDecarreras(Vehiculo):
    def __init__(self):
        pass
    def acelerar(self):
        print("Acelerando el Auto DE carreras")
class Moto(Vehiculo):
    def __init__(self):
        pass
    def acelerar(self):
        print("presionando siguiendo acelerando")
class Piloto:
    def __init__(self, vehiculo:Vehiculo) -> None:
        self.vehiculo = vehiculo
    def conducir(self):
        self.vehiculo.acelerar()
Auto_de_carreras = AutoDecarreras()
piloto = Piloto(AutoDecarreras())
piloto.conducir()