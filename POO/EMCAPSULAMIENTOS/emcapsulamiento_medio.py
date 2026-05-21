#🩻 Las Especificaciones del DesafíoVas a crear una clase llamada CajaRegistradora. El dinero no puede ser visto por nadie desde afuera
#.⚠️ Las 4 Reglas del Rompecabezas:La Bóveda Invisible: En el constructor (__init__), guarda la variable __dinero
#e inicialízala en 0 [INDEX_3]. Si alguien hace print(objeto.__dinero), la terminal de Windows debe explotar con un AttributeError
#.El Registro de Auditoría (Tu memoria de colmena): Fuera del constructor, crea una lista compartida llamada historial_transacciones = [] 
#. Cada vez que el dinero cambie, debes guardar un texto en este saco que describa el movimiento
#(ejemplo: "Depósito de 500", "Retiro de 200") [INDEX_3].La Aduana de Entrada (Setter - Depositar):
#Crea el método depositar(self, cantidad) . Debe pasar por un filtro: Solo se aceptan cantidades mayores a 0
#Si es válida, se suma al __dinero y se registra en el historial La Aduana de Salida (Setter - Retirar):
#Crea el método retirar(self, cantidad) Aquí está la trampa difícil: Debes meter una Cláusula de Guarda en una sola línea horizontal
#Si la cantidad a retirar es mayor que el __dinero que hay en la bóveda, debes lanzar un raise ValueError("Fondos insuficientes")
#en el acto, bloqueando el retiro y guardando la etiqueta "ALERTA: Intento de sobregiro" en tu historial de colmena.
class CajaRegistradora:
    historial_transacciones = []
    def __init__(self):
        self.__dinero = 0
    def deposito(self, cantidad):
        if cantidad <= 0:
            return print("ERROR")
        else:
            self.__dinero += cantidad
            print("deposito exitoso")
            self.historial_transacciones.append(f"DEPOSITO DE {cantidad}")
    def retirar(self, cantidad):
        if self.__dinero < cantidad: raise ValueError("FONDOS INSUFICIENTES")
        else:
            self.__dinero -= cantidad
            print("retiro exitoso")
            self.historial_transacciones.append(f"RETIRO DE {cantidad}")
caja = CajaRegistradora()
while True:
    empleado = input("[DEPOSITO] [RETIRAR] [HISTORIAL] [SALIR]: ").lower().strip()
    if empleado == "deposito":
        try:cantidad = int(input("Cantidad de: "))
        except ValueError:
            print("ERROR ESE NUMERO NO EXISTE")
        else:caja.deposito(cantidad)
    elif empleado == "retirar":
        try:cantidad = int(input("cantidad de: "))
        except ValueError:print("ESE NUMERO NO EXISTE")
        else:
            try:caja.retirar(cantidad)
            except ValueError:print("CAJA VACIA")
    elif empleado == "historial":
        for i in caja.historial_transacciones:
            print(i)
    elif empleado == "salir":
        print("descanse")
        break
    else:
        print("esa opcion no ay aqui bro")

