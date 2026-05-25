#🩻 Las Especificaciones del Desafío: El Escudo de Alertas Vas a crear una clase abstracta inmaterializable y una sola clase hija
# real que cumpla el contrato [INDEX_3].⚠️ Las 3 Reglas del Circuito:El Plano Fantasma (ABC):
#Crea una clase abstracta llamada AlertaBase La Orden Obligatoria (@abstractmethod):
#Adentro de esa clase, define el método obligatorio llamado def lanzar(self): con un simple pass vacío
#El Hijo Obediente: Crea una clase hija llamada AlertaHacker que herede de AlertaBase y cumpla la ley escribiendo su propio método
#lanzar(self) para que imprima en la pantalla: "🚨 [SISTEMA] ¡Intruso detectado en la RAM!"
from abc import ABC, abstractclassmethod
class AlertaBase(ABC):
    def __init__(self):
        pass
    @abstractclassmethod
    def lanzar(self):
        pass
class AlertaHacker(AlertaBase):
    def __init__(self):
        pass
    def lanzar(self):
        print("sistema intruso detectado en la RAM")
Alerta = AlertaHacker()
Alerta.lanzar()