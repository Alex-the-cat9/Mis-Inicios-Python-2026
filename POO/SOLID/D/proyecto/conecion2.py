#maestro.IA:Archivo 2: conexion2.py (El Chasis del Exoesqueleto - LA UNIÓN D)
#Su única responsabilidad (S): Manejar la física del traje sin saber qué motor tiene instalado por defecto
#Tu misión: Crea la clase Exoesqueleto.La Ley de la D (Inversión en __init__):
#El constructor no puede crear el reactor adentro Debe recibirlo desde el mundo exterior como un parámetro:
#def __init__(self, nucleo_inyectado):
#    self.posicion = 0
    # 🔑 LA COUPLING D: Guardas la clase viva en tu casillero para no depender de ella
#    self.fuente_poder = nucleo_inyectado 
#Usa el código con precaución.Crea el método def avanzar(self, pasos: int) -> str:
#Este método debe llamar internamente a self.fuente_poder.proveer_energia(pasos * 2).
#Si hay energía, suma los pasos a self.posicion y devuelve el reporte en texto plano [INDEX_3].
import conecion1
class Exoesqueleto:
    def __init__(self, nucleo_inyectado:conecion1.CeldaSolar) -> None:
        self.posicion = 0
        self.funte_poder = nucleo_inyectado
    def avansar(self, pasos:int) -> str:
        aguila = self.funte_poder.proeveer_energia(pasos * 2)
        return f"se iso un total de:{aguila} pasos"
    