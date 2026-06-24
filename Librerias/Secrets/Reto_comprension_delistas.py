#🖥️ El Reto: El Generador de Llaves de Cifrado Simétrico (AES-Keygen)
#En ciberseguridad, los algoritmos como AES (usados para cifrar discos duros o chats de WhatsApp) no usan contraseñas comunes.
#Usan cadenas largas divididas en bloques, pero con una regla estricta:
#combinan bloques de letras y bloques de números por separado para que un atacante no pueda encontrar patrones fácilmente.
#Vas a programar un Keygen que genere una llave con la siguiente estructura exacta:[NÚMEROS]-[LETRAS]-[NÚMEROS]-[LETRAS]
#(Ejemplo: 9032-KOPQ-1480-WXYZ)Requerimientos del código:Crea tu clase privada con su contraseña de acceso como hiciste 
#antes. Dentro del constructor de tu clase, debes tener dos cadenas de elementos privadas distintas:self.__letras:
#Solo letras mayúsculas (ej: "ABCDEFGHIJKLMNOPQRSTUVWXYZ").self.__numeros: Solo números (ej: "0123456789")
#Una vez superado el acceso, debes usar una sola línea de comprensión de listas (List Comprehension)
#para fabricar la estructura.
#Pista de Hacker: No puedes usar un range(4) simple porque los bloques van alternados (uno de números y uno de letras).
#Tendrás que crear los 4 bloques de 4 caracteres directamente dentro de los corchetes [] llamando a choice
#con la lista que corresponda.Une los 4 bloques resultantes usando el pegamento "-".join().
from secrets import choice
class Privada:
    def __init__(self):
        self.__letras = "QWERTYUIOPLKMNJHBGVFCDXSZA"
        self.__numeros = "0123456789"
    def verificar(self):
        acceso = input("Di el acceso: ").strip()
        if acceso == "A-10":
            estructura: list[str] = []
            for _ in range(2):
                estructura.append("-".join(["".join(choice(self.__numeros) for _ in range(4)), "".join(choice(self.__letras) for _ in range(4))]))
            return estructura
        else:
            print("no vereficado")
privado = Privada()
aguila = "-".join(privado.verificar())
print(f"su token es:{aguila}") 