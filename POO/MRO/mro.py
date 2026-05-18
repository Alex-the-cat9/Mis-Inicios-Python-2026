#🩻 Las Especificaciones del DesafíoTienes 5 clases independientes en el laboratorio: FiltroIP, Firewall,
#BaseDatos, Logs y el hijo SistemaSeguro.Quiero que escribas el código en tu VS Code de tal forma que, al ejecutar
#print(SistemaSeguro.__mro__), la terminal de Windows te imprima exactamente este orden de fila india en la RAM
#[INDEX_3, INDEX_36]:[SistemaSeguro, FiltroIP, Firewall, BaseDatos, Logs, object]⚠️
#Las 3 Reglas del Rompecabezas:Clase BaseDatos: Debe heredar en vertical de la clase Logs [INDEX_31]
#.Clase FiltroIP: Debe heredar en vertical de la clase Firewall [INDEX_31].Clase SistemaSeguro (El Hijo):
#Debe heredar en horizontal de dos padres en su paréntesis utilizando herencia múltiple horizontal
#[INDEX_31, INDEX_36]. Tú debes decidir a quién poner a la izquierda y a quién a la derecha para que el GPS del MRO
#calcule la ruta exacta del log de arriba [INDEX_36]
class Firewall:
    pass
class FiltroIP(Firewall):
    pass
class Logs:
    def final(self):
        print("punto final")
class BaseDatos(Logs):
    pass

class SistemaSeguro(FiltroIP,BaseDatos):
    pass
variable = SistemaSeguro()
variable.final()
print(SistemaSeguro.mro())
#Alex:easy