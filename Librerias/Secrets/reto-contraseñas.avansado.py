from secrets import choice
from sys import exit

class Codigo_PRIVADO:
    def __init__(self) -> None:
        # ELEMENTOS privados
        self.__Elementos: str = "AIQOLD10039MCNAIAWOWLWOWOLEAUWAMFKIB00##4=@3JA7/29)RG*-AP:,A?¡¿}GAN|MFA,K}FA'VZ<>JG+-"
        self.__contraseña: str = "A-5"
        
    def acceso(self) -> str:
        Contraseña = input("Si tiene acceso diga la contraseña: ").strip()
        if Contraseña == self.__contraseña:
            print("Bienvenido, le daremos los elementos.")
            return self.__Elementos
        else:
            print("🚨 HACKER de sombrero negro detectado. expulsando del sistema...")
            exit()

Base_de_codigo = Codigo_PRIVADO()
aguila = Base_de_codigo.acceso()
#el cambio aqui vi que hace una lista un join texto choice aguila agarra 4 caracteres de aguila y otro for que diga que va hacer eso 3 veces
estructura: list[str] = ["".join(choice(aguila) for _ in range(4)) for _ in range(3)]
final: str = "-".join(estructura)
print(f"Su clave de licencia final es: {final}")