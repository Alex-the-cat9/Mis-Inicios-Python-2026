from hashlib import sha256
def dar_hahs(texto:str):
    if len(texto) <= 0:
        return "incorrecto"
    return sha256(texto.encode()).hexdigest()
convertir = input("Di el texto que quieres convertir: ")
contraseña = dar_hahs(convertir)
print(contraseña)