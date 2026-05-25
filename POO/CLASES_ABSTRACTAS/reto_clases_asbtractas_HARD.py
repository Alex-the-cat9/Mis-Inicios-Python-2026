#🩻 PLIEGO DE CONDICIONES: EL NÚCLEO BANCARIO DE CONTROLEl Scenario:
#Eres el Arquitecto Principal de un sistema financiero. Tienes dos tipos de operaciones en los servidores:
#RetiroCajero y TransferenciaCrypto. Quieres garantizar que cualquier transacción que se añada en el multiverso cumpla
#obligatoriamente con dos pasos: validar la seguridad y procesar el dinero [INDEX_3].Tu Misión:Diseña una estructura de clases
#abstractas donde el padre imponga la ley marcial de nombres a las operaciones hijas 📐 Las 3 Reglas del Búnker Financial:
#El Supervisor Inmaterial (BaseTransaccion): Crea una clase abstracta llamada BaseTransaccion que herede de abc.ABC 
#Debe obligar a sus hijos a implementar dos métodos abstractos:def validar_seguridad(self):
#def procesar_monto(self): [INDEX_3]Los Operadores Concretos (Las Clases Hijas): Crea dos clases hijas que hereden de tu plano base:
#RetiroCajero: Su método de seguridad debe imprimir un mensaje de escaneo de huella o tarjeta Su método de monto debe imprimir
#cuánto dinero físico está saliendo TransferenciaCrypto: Su método de seguridad debe imprimir un mensaje de verificación de firma 
#digital o llave privada. Su método de monto debe imprimir cuántos tokens se están moviendo por la red blockchain El Despachador
#Universal: Escribe una función independiente llamada ejecutar_transaccion_bancaria(objeto_transaccion)
#Esta función debe recibir cualquier instancia hija y, dentro de su bloque, disparar los dos métodos en orden vertical:
#primero valida la seguridad y luego procesa el monto [INDEX_3].
import abc
class BaseTransaccion(abc.ABC):
    @abc.abstractmethod
    def validar_seguridad(self):
        pass
    @abc.abstractmethod
    def procesar_monto(self):
        pass
class RetiroCajero(BaseTransaccion):
    def __init__(self):
        super().__init__()
        self.seguridad = []
        self.acceso = []
        self.__llave_de_seguridad = "A-28B"
    def validar_seguridad(self):
        if True in self.acceso:
            print("no necesita volver aqui ya tiene acceso concedido")
            raise PermissionError
        if "bloqueado" in self.seguridad:
            print("CUENTA SUSPENDIDA")
            raise PermissionError
        user = input("escibre la llave de seguridad deve ser exacto: ")
        if user == self.__llave_de_seguridad:
            print("perfecto la llave es correcta te dejamos")
            self.acceso.append(True)
        else:
            if 1 in self.seguridad:
                print("Se lo advertimos ahora su cuenta sera suspendida")
                self.seguridad.append("bloqueado")
                raise PermissionError
            print("LLAVE INCORRECTA si vuelve a preguntar su cuenta estara suspendida por sospecho de robo")
            self.seguridad.append(1) 
            raise PermissionError
    def procesar_monto(self):
        if True in self.acceso:
            try:monto = int(input("cuanto quieres sacar en tu cuenta de banco [ADVERTENCIA:solo numeros]: "))
            except ValueError:
                print("porfavor era solo numeros")
            else:
                print(f"el monto {monto} fue sacado exitosamente")
        else:
            print("primero deve pasar por validar seguridad para sacar dinero")
    @property
    def Recuperar_cuenta(self):
        print("lamentamos que su cuenta aya sido robada oh suspendida")
        print("vamos a pasar por una entrevista para ver si eres dueño legitimo de la cuenta...")
        print("exacto lo eres te devolveremos su contraseña")
        return self.__llave_de_seguridad
    @Recuperar_cuenta.setter
    def contraseña(self, nuevo):
        if True in self.acceso:
            nuevo = input("bueno ya tienes acceso puedes decir tu nueva contraseña: ")
            self.__llave_de_seguridad = nuevo
            print("cambiado con exito")
        else:    
         user = input("necesitamos que nos diga la contraseña para poder cambiarla: ")
         if user == self.__llave_de_seguridad:
            nuevo = input("perfecto diganos su nueva contraseña: ")
            self.__llave_de_seguridad = nuevo
            print("cambiado con exito")
         else:print("incorrecto...")
banco = RetiroCajero()
while True:
    print("que deseas hacer: [Validar(vereficamos si es el dueño)] [Recuperar(recupera tu cuenta)] [nueva(que es nueva contraseña)]")
    user = input("oh deceas [procesar(que es procesar el monto)] o [salir] tu eliges: ").lower()
    if user == "validar":
        try:banco.validar_seguridad()
        except PermissionError:
            pass
    elif user == "recuperar":
        aguila = banco.Recuperar_cuenta
        print(f"su contraseña:{aguila}")
    elif user == "nueva":
        banco.contraseña = None
    elif user == "procesar":
        banco.procesar_monto()
    elif user == "salir":
        break
    else:
        print("esa opcion no existe")
    

    

    

