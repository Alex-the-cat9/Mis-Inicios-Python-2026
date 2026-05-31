#Alex:entonces para que un niño de 10 entienda es como:La son 2 cosas que puedes usar pero primero aprenderas
#con la mas facil las clases abstractras la o es como la clase abstracta es tu plano es cerrado y las demas clases
#que creas pero que hereden del cerrado son abiertos puedes modificarlos
#si en solid la ley de la O es tipo deci en codigo:es una clase abstracta no se puede tocar si se toca todas sus clases hijas
#fallan y la terminal estara miles de errores letras rojas pero la clases hijas de la clase abstractas si son modificables 
#Ejemplo:(clase abstracta:auto [clase hija hereda de abstracta y es un auto toyota] tiene la misma cualidades de un auto su
#misma funcion solo que se modifico como su diseño oh sus funciones igual con ferrari lamboryini oh otras marcas de auto y en
#ARCHIVOS: un archivo.py que adentro esta una clase abstracta:este archivo esta con contraseña intocable no se puede tocar  y si
#un hacker lo toca y modifica todo el servidor muere por error de syxtancis oh tal vez un raise que pudo meter el hacker ese archivo
#es una clase abstracta que da datos a otros archivos.py pero los otros archivos .py si se pueden tocar y modificar a tu gusto pero
#el principal/main no (en pocas palabras el problema no es que el padre de alarma oh borre el servidor el problema es el contrato que
#tiene el padre con las clases hijas que exigen su herencia y si no lo tienen causa error)
# El tambor de la pistola con las balas que quedan
import abc
class vehiculo(abc.ABC):
    @abc.abstractmethod
    def viajar(self, distancia):
        pass
    