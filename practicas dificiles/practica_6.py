#Tu Misión: El Generador de Códigos de un Solo Uso (OTP)Debes escribir un script completamente desde cero, sin plantillas,
#que cumpla con estas tres especificaciones técnicas estrictas:Generación Segura (generate_otp):Crea una función que no reciba parámetros.
#Debe generar un código de verificación que consista exactamente en 6 dígitos numéricos (un string, por ejemplo: "482019").
#La Regla de Élite: Está prohibido usar el random de juguete. Debes obligar al sistema a usar la licuadora del kernel invocando 
#secrets.choice() dentro de un bucle o una comprensión de lista para extraer cada dígito de forma impredecible.
#Persistencia del Token:Crea un almacén seguro en memoria (un diccionario privado o una estructura controlada) llamado 
#PENDING_VERIFICATIONS.Tu función debe guardar ese código de 6 dígitos como una clave (key) dentro del diccionario, y asignarle como valor el estado 
#"PENDING" (ej: {"482019": "PENDING"}).La función debe retornar el código generado.
#Validación Atómica (verify_otp):Crea una segunda función que reciba el código que el usuario introduce en la pantalla.Debe buscar el código en 
#PENDING_VERIFICATIONS.
#Si el código existe y su estado es "PENDING", debe cambiar el estado en el diccionario a "USED" (para que nadie pueda reutilizar el mismo código)
#y retornar True.Si el código no existe, es incorrecto o ya fue usado, debe retornar False de inmediato de forma fría y genérica.Entorno de Control 
#(__main__):Simula el flujo: genera un código válido, valídalo con éxito (debe dar True), e inmediatamente intenta validarlo una segunda vez
#(debe dar False porque ya cambió a "USED").Tus Reglas Corporativas Sin atajos: Diseña tú mismo la estructura en una hoja en blanco.
#Nomenclatura limpia: Todo en inglés técnico de infraestructura (ej: otp_code, verification_store, is_valid).
import secrets
from typing import Final
class system:
    def __init__(self):
        self.__numers: Final[list[str]] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
        self.__PENDING_VERIFICATIONS = {}
    def generate_otp(self):
        otp_code = 2
        while otp_code in self.__PENDING_VERIFICATIONS:
            otp_code: Final[str] = "".join(secrets.choice(self.__numers) for _ in range(6))
        self.__PENDING_VERIFICATIONS[otp_code] = "PENDING"
        return otp_code
    def verify_otp(self, codigo:str):
        if codigo not in self.__PENDING_VERIFICATIONS:
            return False
        if self.__PENDING_VERIFICATIONS[codigo] == "PENDING":
            del self.__PENDING_VERIFICATIONS[codigo]
            return True
        else:
            return False
if __name__ == "__main__":
    System = system()
    code = System.generate_otp()
    message = System.verify_otp(code)
    if message:
        print("Your code worked")
    else:
        print("Your code no worked.")
    message = System.verify_otp(code)
    if message:
        print("Your code worked")
    else:
        print("Your code no worked")
    message = System.verify_otp("932123")
    if message:
        print("Your code worked")
    else:
        print("Your code no worked")
