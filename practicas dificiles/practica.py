#El Escenario: El Cajero Automático "Ciego"Imagina que estás diseñando la lógica para un cajero automático.
#El sistema sigue exactamente estos tres pasos en orden cuando alguien quiere sacar dinero:
#Paso 1: El usuario mete su tarjeta y digita que quiere retirar $100.
#Paso 2: El cajero físico abre la ranura y le entrega los $100 en efectivo al usuario.
#Paso 3: El sistema del cajero se conecta a internet, busca la cuenta del usuario en el banco y le resta los $100 de su saldo.
from typing import Dict, TypedDict
class account(TypedDict):
    Name:str
    US:int
def User_created(Name:str, US:int):
    if len(Name) <= 2:
        raise ValueError("short name")
    return account(Name=Name, US=US)
One_User = User_created("Alex", 400)
Prohibid: list[str] = []
def cash(User_account: account, US:int):
    Limited = User_account["US"] - US
    if Prohibid.count(User_account["Name"]) >= 3:
        raise PermissionError(f"{User_account} Prohibid open machin")
    if US <= 0:
        Prohibid.append(User_account["Name"])
        raise ValueError("US invalid")
    if User_account["US"] < US or Limited < 100:
        Prohibid.append(User_account["Name"])
        raise ValueError("insufficient US")
    else:
        User_account["US"] -= US
        return US
View = cash(One_User, 300)
print(One_User)
print(View)
#El Despertar de la Mentalidad Defensiva (Tus Logros)Inversión de Flujo Catastrófico: Empezaste con un diseño ciego donde
#el dinero se entregaba antes de actualizar el sistema (un regalo para los atacantes). Aprendiste a precalculación de estados
#futuros (Limited = balance - US), bloqueando la transacción antes de aplicar cambios irreversibles en memoria.Destrucción de
#Variables Globales Mutables: Eliminaste el uso de global Banco, una práctica nefasta que habría causado colisiones de datos destructivas
#en entornos concurrentes. Migraste el manejo de datos a estructuras aisladas (TypedDict).Comprensión del Ciclo de Vida de la Memoria:
#Pasaste de crear una lista local que se borraba a cada segundo, a comprender cómo colocar estructuras en el ámbito adecuado para que
#el sistema pudiera recordar y rastrear la persistencia de un ataque por fuerza bruta.2. Los Errores Críticos que CorregimosLa Inyección
#por Signo Invertido: Tu código inicial aceptaba retiros negativos (-5000), lo que se traducía en sumas artificiales de dinero. Te enseñé
#a implementar filtros de mitigación de inputs basura (if US <= 0).La Paradoja de los Operadores Relacionales: Tu lógica matemática fallaba
#al usar < y <= de forma caótica, bloqueando a clientes legítimos que querían retirar montos válidos. Aprendiste que en sistemas financieros
#un solo carácter de diferencia altera el balance por millones.La Trampa de Complejidad Algorítmica (O(N)): Intentaste mitigar ataques usando
#una lista global acumulativa (Prohibid.append). Te demostré cómo eso genera fugas de memoria (Memory Leaks) y cuellos de botella en la CPU,
#obligándote a mirar hacia las tablas hash (Dict) de complejidad constante O(1).