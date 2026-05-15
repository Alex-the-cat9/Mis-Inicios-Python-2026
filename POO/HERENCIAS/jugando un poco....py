import sys
class personaje:
    def __init__(self, vida, daño):
        self.vida = vida
        self.daño = daño
    def entrar_en_lucha(self):
        print("personaje comun ataca")
        return self.daño
mochila = {"Almas":0}
class Alex(personaje):
    def __init__(self, vida, daño, arma):
        super().__init__(vida, daño)
        self.arma = arma
    def atacar(self):
        if self.arma <= 0:
            return self.daño
        else:
            combinacion = self.arma + self.daño
            return combinacion
personaje_comun = personaje(20,20)
alex = Alex(50,20,2)
dañ0 = personaje_comun.entrar_en_lucha()
alex_daño = alex.atacar()
print("Alex te ataca una persona as algo")
while True:
    que = input("[luchar] [huir]: ")
    if que == "luchar":
         print(f"le isiste daño el tenia:{personaje_comun.vida}")
         personaje_comun.vida -= alex_daño
         print(f"y ahora tiene:{personaje_comun.vida}")
         if personaje_comun.vida <= 0:
             print("GANASTE")
             mochila["Almas"] += 1
             break
    else:
        print("TE ATACAM")
        print(f"te isieron daño tenias esta vida:{alex.vida}")
        alex.vida -= dañ0
        print(f"y ahora tienes:{alex.vida}")
        if alex.vida <0:
            print("moriste...")
            sys.exit()
