#Crea un archivo nuevo en tu VS Code llamado test_liskov.py
#Diseña una clase abstracta padre que exija un método para procesar una contraseña Usa los dos puntos (:) 
#para obligar a que la entrada sea estrictamente un texto plano (str) [INDEX_3].Usa la flecha (->) 
#para prometerle al receptor que la salida será sí o sí un valor booleano (bool) Crea la Clase Hija A (La Fiel):
#Programa el método respetando exactamente la misma aduana: recibe texto plano (str) y devuelve un booleano
#(True o False) [INDEX_3].Crea la Clase Hija B (La Traidora): Sabotea el contrato molecular a propósito para ver
#si tu radar funciona [INDEX_3]. Modifica la firma del método para que reciba el texto plano, pero haz que devuelva
#un número entero (int) o un diccionario en lugar del booleano prometido [INDEX_3].Ejecuta la auditoría:
#Guarda el archivo, abre tu PowerShell de Windows y escribe el comando exacto [INDEX_3]:
#import abc
#class Prueba(abc.ABC):
#    @abc.abstractmethod
#    def preparacion(self, entrada:str) -> bool:
#        pass
#class Fiel(Prueba):
#    def __init__(self):
#        pass
#    def preparacion(self, entrada:str) -> bool:
#        print(f"se entro esta entrada:{entrada} es correcta")
#        return True
#class Revelde(Prueba):
#    def __init__(self):
#        pass
#    #def preparacion(self, entrada:str) -> bool:#esta en rojo esta linea
    #    print("somos reveldes oh si")#esta en rojo esta linea
#hija_fiel = Fiel()
#hija_revelde = Revelde()
#aguila = hija_fiel.preparacion("preparandoo")
#if aguila:
#    print("aguila registrando la primera hija cumplio su trabajo")
#aguila = hija_revelde.preparacion(10)#esta en rojo esta linea
#if aguila:
#   print("la segunda hija cumplio su trabajo")        

