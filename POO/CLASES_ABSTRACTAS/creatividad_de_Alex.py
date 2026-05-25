#El Desafío del Sistema de Notificaciones Universal
#El Escenario:
#Eres el arquitecto de un nuevo sistema de notificaciones que debe ser capaz de enviar mensajes a diferentes tipos de plataformas:
#correo electrónico, SMS y notificaciones push (como las de una app móvil). Quieres asegurarte de que, sin importar qué tipo de
#notificación se añada en el futuro, siempre tenga una forma de ser enviada.
#Las Especificaciones del Desafío:
#Vas a crear una estructura de clases que permita gestionar distintos tipos de notificaciones de manera flexible y extensible.
#Las 3 Reglas del Circuito:
#El Maestro de las Notificaciones (NotificationBase):
#Crea una clase abstracta llamada NotificationBase.
#Esta clase debe tener un método abstracto llamado send(self). Este método no debe tener implementación en la clase base;
#solo debe definir que las clases hijas deben implementarlo.
#Los Mensajeros Especializados:
#Crea tres clases hijas concretas que hereden de NotificationBase:
#EmailNotification: Deberá implementar su método send(self) para imprimir: "Enviando notificación por correo electrónico...".
#SMSNotification: Deberá implementar su método send(self) para imprimir: "Enviando notificación por SMS...".
#PushNotification: Deberá implementar su método send(self) para imprimir: "Enviando notificación push a la aplicación...".
#El Director de Orquesta (Sistema de Envío):
#Escribe una función llamada send_notification(notification_instance).
#Esta función recibirá cualquier instancia de una clase que herede de NotificationBase
#(es decir, EmailNotification, SMSNotification, o PushNotification).
#Dentro de la función, simplemente llama al método send() de la instancia recibida.
#El Objetivo:
#Demostrar que puedes crear una jerarquía de clases donde un método abstracto fuerza la implementación en las clases hijas,
#y que puedes diseñar una función que opere genéricamente sobre cualquiera de esas clases hijas sin importar cuál sea específicamente.
#Tu Tarea:
#Escribe el código Python que implemente estas clases y la función send_notification. Luego, crea instancias de cada tipo de notificación
#y pásalas a la función send_notification para ver que todo funciona correctamente.
from abc import ABC, abstractclassmethod
import abc
class NotificationBase(abc.ABC):
    @abc.abstractmethod
    def send(self):
        pass
class EmailNotification(NotificationBase):
    def send(self):
        print("Enviando notificacion por correo electronico...")
class SMSNotification(NotificationBase):
    def send(self):
        print("Enviando notificacion por SMS-..")
class PushNotification(NotificationBase):
    def send(self):
        print("Enviando notificacion push a la aplicacion....")
def send_notification_instance(instance):
    instance.send()
Email = EmailNotification()
SMS = SMSNotification()
Push = PushNotification()
while True:
    try:user = int(input("[1:Email] [2:SMS] [3:Push] [4:salir] escribe un numero: "))
    except ValueError:
        print("SOLO UN NUMERO")
    if user == 1:
        send_notification_instance(Email)
    elif user == 2:
        send_notification_instance(SMS)
    elif user == 3:
        send_notification_instance(Push)
    elif user == 4:
        break
    