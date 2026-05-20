#🩻 Las Especificaciones del DesafíoCrea una clase llamada ServidorMilitar. Dentro del constructor, debes guardar una variable llamada
# ip con el valor "192.168.1.1".⚠️ Las 3 Reglas del Rompecabezas:Blindaje Absoluto: Debes aplicar el escudo "Muy Muy Privado"
#a la variable de la IP para que si alguien intenta hacer print(objeto.ip) o print(objeto.__ip) desde afuera, la terminal de Windows
#explote con un AttributeError [INDEX_3].La Aduana de Lectura (Getter): Crea un método llamado obtener_ip(self) [INDEX_39]. Este método
#debe retornar el texto limpio de la IP para las consultas legales [INDEX_3].La Aduana de Ataque (Setter): Crea un método llamado
#modificar_ip(self, nueva_ip) [INDEX_39]. El método debe tener un cortafuegos: Solo aceptará el cambio si la nueva IP comienza
#con el texto "192.". Si el usuario intenta inyectar una IP que empiece con otra cosa (ejemplo: "10.0.0.1")
#el sistema debe mostrar un letrero de "🚨 [SISTEMA] ¡Intento de desvío de red bloqueado!" y NO cambiará el valor de la bóveda [INDEX_3].
class ServidorMilitar:
    alarm = []
    def __init__(self):
        self.__Ip = "192.168.1.1"
    def obtener_Ip(self):
        return self.__Ip
    def modificar_ip(self, nueva_ip):
        if True in self.alarm:
            return print("INTENTO DE DESVIO DE RED BLOQUEADO")
        else:
         self.__nueva_ip = nueva_ip
         if "192" in self.__nueva_ip:
             print("ACEPTADO")
             self.__Ip = self.__nueva_ip
         else:
             print("INTENTO DE DESVIO DE RED BLOQUEADO")
             self.alarm.append(True)

Militar = ServidorMilitar()
try:print(Militar.__Ip)
except AttributeError:
    print("BLOQUEANDO entrada")
Militar.modificar_ip("121")
Militar.modificar_ip("192")