#Alex:ahora dame un reto dificil de choice y choices puedes poner poo funciones si quieres o clases abstractas
#Ramdon_maestro.IA:¡Me encanta tu entusiasmo! Ha llegado el momento de subir el nivel al máximo.
#Vamos a construir un sistema simulado para un videojuego de rol (RPG).

#Este reto combina Programación Orientada a Objetos (POO), Clases Abstractas, Mapeo con Diccionarios,
#y por supuesto, el uso estratégico de choice y choices para manejar el azar de los combates.
#1:La clase abstracta (personaje)
#deve importar ABC y abstracmethod del modulo abc crea clases abstractas llamada PERSONAJE que tenga
#un constructor (__init__) con contribuciones (str:nombre) y (int:vida)
#un metodo abstracto llamada def atacar(self, enemigo)
#. Las Clases Hijas (Los Guerreros)Crea tres clases que hereden de Personaje:
#Mago:Su ataque base hace 15 de daño. Pero tiene una habilidad especial: cada vez que ataca, tiene un lista de hechizos
#["Fuego", "Hielo", "Rayo"]. Debe usar choice para elegir un elemento estético del hechizo al atacar.
#Asesino: Su ataque base hace 10 de daño. Sin embargo, tiene probabilidad de golpe crítico. Al atacar, debes usar choices
#con pesos (weights). Tienes dos opciones de golpe:
#["Normal", "Crítico"]. El golpe Normal hace 10 de daño (80% de probabilidad), el golpe Crítico hace 30 de daño 
#(20% de probabilidad).
#Curandero: Su ataque hace siempre 8 de daño, pero cada vez que ataca, usa choice para elegir curarse a sí
#mismo entre [0, 5, 10] puntos de vida adicionales.
#3. El Diccionario de Reglas y el Bucle de Batalla
#Crea un diccionario que sirva para emparejar a los peleadores o registrar eventos.
#En tu código principal, introduce a los personajes en una lista.
#Crea un bucle donde, en cada ronda, un personaje sea elegido con choice para atacar a otro personaje de la lista
#(¡asegúrate de que no se ataque a sí mismo!).El juego termina cuando solo quede un personaje con vida (vida > 0).
from abc import ABC, abstractmethod
from random import choice, choices 
class Personaje(ABC):
    def __init__(self, nombre:str, vida:int):
        pass
    @abstractmethod
    def atacar(self, enemigo):
        pass
    def __str__(self):
        return f"Nombre:{self.nombre} | Vida:{self.vida}"
class Mago(Personaje):
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.clase = "mago"
    def atacar(self, enemigo):
        elementos = ["Fuego", "Hielo", "Rayo"]
        elegido = choice(elementos)
        if elegido == "Fuego":
            print(f"elegido QUEMADURA quemate {enemigo.nombre} se causo 15 de daño y 10 de daño quemadura total:25 daño")
            enemigo.vida -= 25
            return 25
        elif elegido == "Hielo":
            hielo = ["hipotermia", "frio"]
            enemigo.vida -= 15
            print(f"Elegido Hielo Congelate {enemigo.nombre} se causo 15 de daño pero ay una probabilidad de matarlo de hipotermia")
            probabilidad = choices(hielo, k=1, weights=[5,95])[0]
            if probabilidad == "hipotermia":
                print("el frio le causo hipotermia se iso un daño critico de 100 puntos de vida")
                enemigo.vida -= 100
                return 100 + 15
            else:
                print("el frio solo le causo frio se iso un daño de 5 de vida")
                enemigo.vida -= 5
                return 15 + 5
        elif elegido == "Rayo":
            print(f"Elegido Rayo electrucutate {enemigo.nombre} se causo 15 de daño y 20 de daño por la electricidad total:35")
            enemigo.vida -= 35
            return 35
    def __repr__(self):
        return f"{self.nombre}:es un mago hace 25 de daño y tiene unas probabilidades de hacerle efectos secundarios de elemntos al enemgio"
class Asesino(Personaje):
    def __init__(self, nombre:str, vida:int):
        self.nombre = nombre
        self.vida = vida
        self.clase = "asesino"
    def atacar(self, enemigo):
        golpes = ["normal", "critico"]
        resultado = choices(golpes, weights=[40,60], k=1)[0]
        if resultado == "normal":
            print("golpe normal isimos 20 de daño")
            enemigo.vida -= 20
            return 20
        elif resultado == "critico":
            print(f"golpe critico isimos:50 de daño")
            enemigo.vida -= 50
            return 50
    def __repr__(self):
        return f"{self.nombre}:asesino tiene una probabilidad de hacer daño critico que quita mucha vida"
class Curandero(Personaje):
    def __init__(self, nombre:str, vida:int):
        self.nombre = nombre
        self.vida = vida
        self.clase = "curandero"
    def atacar(self, enemigo):#aqui quiero cambiar un poco las reglas porque el juego esta resultando divertido y de aqui a adelante
        #lo are yo
        print("curando...")
        curaciones = [20,40,60]
        resultado = choices(curaciones, k=1, weights=[30,40,60])[0]
        enemigo.vida += resultado
        print(f"se curo:{resultado} a {enemigo.nombre}")
        return resultado
    def __repr__(self):
        return f"{self.nombre}:curandero cuando ataca puede curar a tus aliados"
        