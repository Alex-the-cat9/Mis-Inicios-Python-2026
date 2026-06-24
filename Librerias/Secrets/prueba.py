import secrets
import string

def generar_password_segura(longitud: int = 12) -> str:
    """Genera una contraseña usando caracteres seguros de forma impredecible."""
    # string.ascii_letters contiene todas las letras (A-Z, a-z)
    # string.digits contiene los números ('0'-'9')
    # string.punctuation contiene símbolos (!, @, #, $, etc.)
    caracteres_validos: str = string.ascii_letters + string.digits + string.punctuation
    
    # Creamos la contraseña eligiendo caracteres uno por uno con secrets.choice
    password: str = "".join(secrets.choice(caracteres_validos) for _ in range(longitud))
    return password

def crear_token_sesion() -> str:
    """Genera un token hexadecimal único para mantener abierta la sesión de un usuario."""
    # token_hex(32) genera una cadena segura de 64 caracteres al azar
    return secrets.token_hex(32)

# --- PRUEBA DEL SISTEMA DE SEGURIDAD ---

print("=== SISTEMA DE SEGURIDAD ACTIVADO ===")
# 1. Generamos una contraseña para el usuario
mi_password = generar_password_segura(16)
print(f"Nueva contraseña segura generada: {mi_password}")

# 2. Generamos su token de sesión único (el que los hackers no podrán adivinar con C++)
mi_token = crear_token_sesion()
print(f"Token de sesión asignado al usuario: {mi_token}")
