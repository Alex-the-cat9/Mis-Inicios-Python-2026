#nuevos archivos un solo archivo es mucho codigo y dificil de leer
class Minion:
    def __init__(self):
        self.nombre = "minion"
        self.vida = 10
    def atacar(self, enemigo):
        enemigo.vida -= 10
        return 10
    def __repr__(self):
        return f"minion hace 10 de daño y tiene 10 de vida ataca junto a su invocador"
    def __str__(self):
        return f"{self.nombre} | {self.vida}"
class Invocador:#Personaje exclusivo
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida
        self.clase = "invocador"
    def atacar(self, enemigo, equipo):
        daño_minions = 0
        minio_ataco = False
        for i in equipo:
            if i.nombre == "minion":
                daño_minions += i.atacar(enemigo)
                minio_ataco = True
        enemigo.vida -= 25
        if minio_ataco:
            return daño_minions + 25
        else:
            return 25
    def invocar(self, equipo):
        minion = Minion()
        equipo.append(minion)
    def __str__(self):
        return f"{self.nombre} | {self.vida}"
    def __repr__(self):
        return f"{self.nombre}: hace 20 de daño minons hacen 10 de daño y tienen 10 de vida minions acumulables ataca junto con sus minions"