#Fase 8: El Autenticador de Sesiones Críticas (Hashing y Salting)
#El Contexto Real:En producción, está estrictamente prohibido guardar contraseñas de usuarios en texto plano dentro de una base de datos o diccionario.
#Si un atacante ejecuta una inyección SQL o roba un respaldo de los datos, conocería las claves de todos los clientes de inmediato.
#Para evitar esto, la industria utiliza algoritmos de Hashing Criptográfico combinados con un Salt (una cadena aleatoria única por usuario)
#para transformar la contraseña en un código irreversible.
#Tu Misión de Diseño (Solo Texto):
#Vas a construir un sistema modular en Python que gestione el registro y la verificación de contraseñas de administradores
#simulando el control de acceso a un servidor
#financiero. Debes escribir el código completamente desde cero cumpliendo con estos requerimientos estrictos de ingeniería:
#Módulo de Registro (register_admin):Crea una función o estructura que reciba un usuario y una contraseña en texto plano.
#Debe generar un Salt aleatorio único utilizando una biblioteca segura (como secrets o os.urandom)
#Debe combinar ese Salt con la contraseña y procesarlos usando el algoritmo criptográfico SHA-256 (disponible en el módulo nativo hashlib de Python)
#para obtener el hash final.Guarda el resultado en un almacén de datos (un diccionario global que actúe como base de datos) indexado por el nombre de usuario
#guardando únicamente el hash generado y el salt utilizado. La contraseña original debe desaparecer de la memoria inmediatamente.
#Módulo de Verificación (verify_admin):Crea una función que reciba el usuario y la contraseña que alguien intenta usar para iniciar sesión.
#Debe buscar al usuario en tu almacén. Si no existe, debe retornar False de inmediato sin dar pistas de si falló el usuario o la contraseña
#(evitando ataques de enumeración).Si existe, debe extraer el Salt original que guardaste para ese usuario específico, combinarlo con la contraseña 
#que están introduciendo en ese momento y volver a calcular el hash SHA-256.Compara el nuevo hash calculado con el hash almacenado. 
#Si coinciden perfectamente, retorna True, de lo contrario retorna False.
#Entorno de Control (__main__):Escribe las pruebas simulando a un usuario legítimo registrándose e iniciando sesión con éxito.
#Simula a un atacante intentando meter una contraseña incorrecta o un usuario inexistente y demuestra cómo tu sistema repele el acceso devolviendo False limpiamente.
#Tus Reglas de Oro:Sin plantillas: Diseña tú mismo los nombres de las funciones, los tipos de datos y el flujo.
#Inglés técnico estricto: Todo el código (variables, métodos, comentarios de control) debe estar escrito en inglés profesional de ciberseguridad.
#Aislamiento: Está terminantemente prohibido usar variables globales mutables desprotegidas; encapsula el estado o usa tipos rígidos.
from secrets import token_bytes
import hashlib
from typing import TypedDict
class UsersegurityData(TypedDict):
    Salt:bytes
    hash:str
class AdminAuthRepository:
    def __init__(self):
        self.__dataBase: dict[str, UsersegurityData] = {}
    def register_admin(self, User:str, password:str):
        salt = token_bytes(16)
        conbined = salt + password.encode("utf-8")
        result = hashlib.sha256(conbined).hexdigest()
        self.__dataBase[User] = {"Salt":salt, "hash":result}
    def verify_admin(self, user:str, password:str) -> bool:
        if user not in self.__dataBase:
            return False
        salt = self.__dataBase[user]["Salt"]
        conbined = salt + password.encode("utf-8")
        result = hashlib.sha256(conbined).hexdigest()
        if result == self.__dataBase[user]["hash"]:
            return True
        else:
            return False
if __name__ == "__main__":
    system = AdminAuthRepository()
    user1 = system.register_admin("Alex", "alexis99")
    User = system.verify_admin("Alex", "alexis99")
    if User:
        print("User logged in")
    else:
        print("error system")
    #test security
    hacker = system.verify_admin("Alex", "alexIs99")
    if hacker:
        print("Alert segurity")
    else:
        print("No alert segurity")