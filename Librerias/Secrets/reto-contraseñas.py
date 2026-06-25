#💻 El Reto: El Generador de Claves de Cifrado (Keygen)
#Imagina que estás auditando un sistema antiguo y necesitas fabricar una herramienta
#(un Keygen) que genere Claves de Licencia para activar un software.
#Las claves de licencia seguras tienen un formato especial dividido por bloques, como las tarjetas de crédito
#o los códigos de videojuegos. El formato exacto que debes generar es este:XXXX-XXXX-XXXX
#(Tres bloques de 4 caracteres, separados por guiones).
#Requerimientos del código:Usa una cadena llamada caracteres que contenga solo letras mayúsculas y números
#(ej: "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789").
#Usa choice() y un for _ in range(4) con "".join() 
#para fabricar un bloque de 4 caracteres pegados (ej: "A8TR").
#Genera tres bloques distintos usando esa misma lógica.
#Finalmente, une esos tres bloques usando un "-".join() para que el resultado final quede exactamente con la 
#estructura XXXX-XXXX-XXXX.Imprime la clave final en la pantalla.
from secrets import choice
from sys import exit
class Codigo_PRIVADO:
    def __init__(self):
        self.__Elementos = "AIQOLD10039MCNAIAWOWLWOWOLEAUWAMFKIB00##4=@3JA7/29)RG*-AP:,A?¡¿}GAN|MFA,K}FA'VZ<>JG+-"
        self.__contraseña = "A-5"
    def acceso(self):
        Contraseña = input("Si tiene acceso diga la contraseña: ")
        if Contraseña == self.__contraseña:
            print("Bienvenido le daremos los elementos")
            return self.__Elementos
        else:
            print("HACKER de sombrero negro detectado")
            exit()
Base_de_codigo = Codigo_PRIVADO()
aguila = Base_de_codigo.acceso()
base1 = "".join(choice(aguila) for _ in range(4))
base2 = "".join(choice(aguila) for _ in range(4))
base3 = "".join(choice(aguila) for _ in range(4))
estructura = [base1, base2, base3]
final = "-".join(estructura)
print(f"su contraseña final es:{final}")