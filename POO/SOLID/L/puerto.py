#EL PLANO DE INGENIERÍA: Todo en un solo archivo puerto.py
#Crea el script e inyecta la corriente eléctrica cumpliendo estrictamente la ley de la L 
#[S]:1. El Plano de Hierro (La Clase Abstracta Base)
#Crea la clase abstracta ContenedorBase(abc.ABC).Diseña el método abstracto obligatorio descargar
#[S].La Aduana Estricta (Tus Acompañantes): Usando el tipado estricta, el método debe exigir que el peso de entrada
#sea sí o sí un número entero (peso: int) y prometer al receptor que sí o sí devolverá un texto plano
#(-> str) [S].2. Las Dos Clases Hijas (Los Reemplazos de Confianza)Hija A (ContenedorComun):
#Recibe la distancia o el peso de forma normal. Ejecuta su método descargar(self, peso: int) -> str
#devolviendo un reporte limpio en texto plano [S].Hija B (ContenedorNuclear):
#Este es un contenedor blindado de alta ciberdefensa [S]. Su código de desactivación secreto
#(self._codigo_nucleo = "9999") debe nacer oculto en su constructor __init__ para proteger la S
#[S]. Su método descargar(self, peso: int) -> str debe recibir exactamente el mismo parámetro
#único que el padre (respetando la L), validar el código por dentro en el silicio,
#y devolver el reporte de radiación en texto plano [S].
#3. El Receptor (Tu Interfaz Interactiva Visual)Abajo de tu archivo, monta una lista de inventario mezclando ambos contenedores
#[S].Crea un bucle for que recorra los contenedores y les meta corriente escribiendo exactamente la misma línea
#de código pasándoles un solo número entero: contenedor.descargar(500) [S].🥷 La Regla Marcial del ÉxitoSi la ContenedorNuclear
#intenta exigir el código de seguridad a través de los parámetros del método descargar(), ¡asesinas la L! Porque romperías el
#enchufe del receptor y harías estallar la terminal de Windows en un TypeError [S]. El código de seguridad
#se procesa por dentro, manteniendo la firma externa idéntica al padre [S].
import abc
from typing import Any#sirve para apagar los radares de mypy pero nose porque lo puse si no lo usare
class ContenerdorBase(abc.ABC):#la clase abstracta padre no tocar
    @abc.abstractmethod#el metodo astracto
    def descargar(self, peso:int) -> str:#descargar nombre peso deve ser un int y deve devolver si o si un str
        pass
class ContenedorComun(ContenerdorBase):#primera clase hija ereda de su padre
    def __init__(self):#el constructor nada que ver no es inportante
        pass
    def descargar(self, peso:int) -> str:#aqui deve entrar un numero entero y si o si deve devolver un texto
        return f"peso del contenedor comun de la base nuclear:{peso}"#aqui devolvio su texxto
class ContenedorNuclear(ContenerdorBase):#aqui se crea la segunda clase hija
    def __init__(self):#constructor
        self._codigo_nucleo = "9999"#este sera el primer atributo que tendra tiene el texto del codigo del nucleo
    def descargar(self, peso:int) -> str:#el metodo del padre astracto  peso deve ser un entero y deve devolver si o si un texto
        return f"codigo del nucleo:{self._codigo_nucleo} con el peso {peso}"#devolvio su texto cumplio
inventario:list[ContenerdorBase] = [ContenedorComun(), ContenedorNuclear()]#ponemos todo en una lista siguiendo em mro
for i in inventario:#un for
    aguila = i.descargar(400)#aguila sera el contenedor comun y luego cambia a contenedor nuclear
    print(aguila)#por cada vuelta le diremos que es lo que registro

