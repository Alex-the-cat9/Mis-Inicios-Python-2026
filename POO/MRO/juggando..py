class Firewall:
    def __init__(self, Firewall):
        self.Firewall = Firewall
    def mostrar_Firewall(self):
        print("todo en orden")
class FiltroIP(Firewall):
    def __init__(self, Firewall, IP):
        super().__init__(Firewall)
        self.IP = IP
    def lista_IP(self):
        listaDeip = ["19281", "18301"]
class Logs:
    def __init__(self, logs):
        self.logs = logs
    def final(self):
        print("logs seguros")
class BaseDatos(Logs):
    def __init__(self, logs, base_de_datos):
        super().__init__(logs)
        self.base_de_datos = base_de_datos
    def base_de_dato(self):
        print("conectado con logs")

class SistemaSeguro(FiltroIP,BaseDatos):
    def __init__(self, sistema):
        super().__init__("FIREWALL", "11112")
        BaseDatos.__init__(self,"122211", "LONG")
        self.sistema = sistema
    def mirar(self):
        print("todo es orden")

variable = SistemaSeguro("XD")
variable.final()

print(SistemaSeguro.mro())
#Alex:easy