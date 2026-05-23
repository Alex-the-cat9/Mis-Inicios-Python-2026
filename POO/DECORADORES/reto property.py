#🩻 Las Especificaciones del Desafío: El Limitador de MotoresVas a crear una clase llamada Droide
#El motor no puede recibir voltajes corruptos ni velocidades negativas desde afuera
#⚠️ Las 3 Reglas del Circuito:La Bóveda Oculta: En el constructor (__init__),
#inicializa la variable muy muy privada self.__velocidad = 0 [INDEX_3].El Atajo de Lectura (@property):
#Crea el método camuflado def velocidad(self): que sirva como el Getter para lanzar la pelota con el return
#El Inyector Aduanero (@nombre.setter): Crea el Setter camuflado para capturar el signo de igual (=)
#Debe tener un Firewall: Solo aceptará el cambio si la nueva velocidad es mayor que 0. Si intentan meter un número negativo o un cero
#el sistema imprimirá "🚨 [CORTAFUEGOS] ¡Velocidad peligrosa bloqueada!" y NO cambiará la bóveda [INDEX_3].
class MotoresVas:
    def __init__(self):
        self.__velocidad = 0
    @property
    def velocidad(self):
        return self.__velocidad
    @velocidad.setter
    def velocidad(self,nueva):
        if nueva <= 0:raise ValueError("error")
        else:
            self.__velocidad = nueva
bot = MotoresVas()
print("Antes del cambio")
aguila = bot.velocidad
print(aguila)
bot.velocidad = 50
print("despues del cambio")
aguila = bot.velocidad
print(aguila)