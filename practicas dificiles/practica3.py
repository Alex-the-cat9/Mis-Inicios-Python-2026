# FASE 5: ARQUITECTURA DE OBJETOS - PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Si quieres dominar FastAPI y los frameworks profesionales, primero tienes que 
# dejar de escribir funciones sueltas y aprender a encapsular datos y lógica 
# dentro de Clases rígidas
# En entornos financieros, la POO se usa para crear "Objetos de Dominio" que se 
# defienden a sí mismos. Una clase mal diseñada permite que cualquiera altere 
# sus propiedades internas desde fuera, corrompiendo el estado del sistema
# ------------------------------------------------------------------------------
# EL RETO DE ENCAPSULAMIENTO: LA CLASE "CUENTA BLINDADA"
# ------------------------------------------------------------------------------
# Vas a construir una clase que represente la cuenta de un banco. Aplicaremos 
# encapsulamiento estricto utilizando atributos privados (los que empiezan con 
# doble guion bajo '__') para que nadie pueda modificarlos directamente sin pasar 
# por los filtros de seguridad.
#
# REGLAS DEL OBJETO:
# 1. Atributos Privados: La clase debe tener dos atributos privados:
#    - '__owner' (str): El nombre del dueño.
#    - '__balance' (int): El saldo en dólares de la cuenta.
# 2. Constructor ('__init__'): Debe recibir el dueño y el depósito inicial. 
#    Si el depósito inicial es menor a $100, lanza un ValueError("INVALID_DEPOSIT").
# 3. Métodos de Acceso (Getters): Crea métodos para *leer* los valores de forma 
#    segura, ya que al ser privados no se pueden leer directamente desde fuera.
# 4. Método de Mutación Segura (Withdraw): Crea un método para restar saldo. 
#    Debe validar que el retiro sea mayor a 0 y que no deje la cuenta con menos 
#    de $100. Si viola las reglas, lanza un PermissionError("DENIED").
from typing import Final

class SecureAccount:
    """
    Clase corporativa encapsulada. 
    Protege el estado financiero mediante el uso de atributos privados.
    """
    def __init__(self, owner: str, initial_deposit: int):
        # 1. Validar que initial_deposit no sea menor a 100.
        if initial_deposit < 100:
            raise ValueError("INVALID_DEPOSIT")
        # 2. Asignar los atributos privados usando '__owner' y '__balance'.
        self.__owner = owner
        self.__balance = initial_deposit
    def get_owner(self) -> str:
        """Devuelve el nombre del dueño legítimo."""
        # Retorna el atributo privado del dueño
        return self.__owner
    def get_balance(self) -> int:
        """Devuelve el saldo actual de forma segura."""
        # Retorna el atributo privado del saldo
        return self.__balance
    def withdraw_cash(self, amount: int) -> int:
        """
        Modifica el saldo interno aplicando las políticas del banco.
        Evita que el balance caiga por debajo de $100 o procese montos negativos.
        """
        # 1. Validar que amount sea mayor a 0.
        if amount <= 0:
            raise PermissionError("DENIED")
        # 2. Validar que el saldo restante no sea menor a 100.
        View: int = self.__balance - amount
        if View < 100:
            raise PermissionError("DENIED")
        # 3. Restar del atributo privado y retornar el monto retirado.
        self.__balance -= amount
        return amount
# --- ENTORNO DE PRUEBAS PARA EVALUAR TU POO ---
if __name__ == "__main__":
    print("=========================================================")
    print("PROBANDO ENCAPSULAMIENTO DE CLASES (POO)")
    print("=========================================================")
    
    # Aquí instanciarás tu clase, probarás un retiro exitoso y 
    try:
        account = SecureAccount("Alex", 200)
        View = account.get_owner()
        US = account.withdraw_cash(50)
        vie = account.get_balance()
    except Exception as error:
        print(f"DETECTED ERROR:{str(error)}")
    else:
        print(f"Name owner:{View}")
        print(f"US dollar withdrawal:{US}")
        print(f"US in account:{vie}")
    # un intento de hackeo/violación de límites atrapando el error.
    try:
        account = SecureAccount("Alex", 200)
        View = account.get_owner()
        US = account.withdraw_cash(200)
        vie = account.get_balance()
    except Exception as error:
        print(f"DETECTED ERROR:{str(error)}")
    else:
        print(f"Name owner:{View}")
        print(f"US dollar withdrawal:{US}")
        print(f"US in account:{vie}")

    print("=========================================================")
