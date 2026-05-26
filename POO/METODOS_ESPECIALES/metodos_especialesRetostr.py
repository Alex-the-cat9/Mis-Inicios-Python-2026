#🩻 Las Especificaciones del Desafío: El Monitor de la IAVas a crear una clase llamada ServidorIA. 
#No queremos que cuando el usuario haga un print() del servidor, la terminal de Windows le aviente ese texto horrible, gris
#y sin sentido de los Juniors (<__main__.ServidorIA object at 0x...>)
#⚠️ Las 2 Únicas Reglas del Circuito:El Constructor Común: En el __init__, guarda el nombre de la IA en la variable
#self.nombre y su estado en self.estado El Camuflaje del Print (__str__): Crea el método especial def __str__(self):
#Su único trabajo es interceptar el print() y lanzar con un return este reporte elegante en horizontal: "🤖 [MONITOR] IA:
#{self.nombre} | Estado: {self.estado}" [INDEX_3].
class ServidorIA:
    def __init__(self, nombre_IA, estado):
        self.nombre_IA = nombre_IA
        self.estado = estado
    def __str__(self):
        return f"IA: {self.nombre_IA} / Estado: {self.estado}"
IA = ServidorIA("Maestro", "Medio")
print(IA)