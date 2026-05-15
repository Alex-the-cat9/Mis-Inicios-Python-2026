class galletita:
    def __init__(self, avena, leche, mantequilla):
        self.avena = avena
        self.leche = leche
        self.mantequilla = mantequilla
    def preparacion(self):
        if self.avena == "avena" and self.leche == "leche" and self.mantequilla == "mantequilla":
          Galleta = "GALLETA COMUN"
        return Galleta
class chocolate(galletita):
    def __init__(self, avena, leche, mantequilla, chocolate):
        super().__init__(avena, leche, mantequilla,)
        self.chocolate = chocolate
    def preparacion(self):
        if self.avena == "avena" and self.leche == "leche" and self.mantequilla == "mantequilla" and self.chocolate == "chocolate":
            combinacion = "GALLETA CON CHOCOLATE"
        return combinacion
class pasas(galletita):
    def __init__(self, avena, leche, mantequilla, pasas):
        super().__init__(avena, leche, mantequilla)
        self.pasas = pasas
    def preparacion(self):
        if self.avena == "avena" and self.leche == "leche" and self.mantequilla == "mantequilla" and self.pasas == "pasas":
            combinacion = "GALLETA LEGENDARIO GALLETA CON PASAS"
        return combinacion
inventario = []
while True:
    usuario = input("necesitamos que ponga los ingredientes correctos para hacer una galleta: ").lower()
    avena = input("necesitamos avena di avena: ").lower()
    leche = input("necesitamos leche di leche: ").lower()
    mantequilla = input("necesitamos mantequilla di mantequilla: ").lower()
    print("preparando...")
    try:
        galleta1 = galletita(avena, leche, mantequilla)
        galleta = galleta1.preparacion()
        inventario.append(galleta)
    except UnboundLocalError:

        print("Falta ingredientes lo iste mal vuelve al inicio")
        continue
    print("perfecto ya isiste tu galleta mira tu inventario")
    print(inventario)
    usuario1 = input("decearias ir a otro nivel?: ").lower()
    if usuario1 == "si":
        print("bien ahora solo necesitamos chocolate")
        chocolat = input("di chocolate: ").lower()
        try:
            galleta2 = chocolate(avena, leche, mantequilla, chocolat)
            galleta_2 = galleta2.preparacion()
            inventario.append(galleta_2)
        except UnboundLocalError:
            print("error vaye al inicio")
            continue
        print("perfecto ahora mire su inventario esta recolectando galletitas")
        print(inventario)
        usuario2 = input("quieres ir al tercer nivel?: ").lower()
        if usuario2 == "si":
            pasa = input("para hacer la galleta legendario di pasas: ").lower()
            try:
                galleta3 = pasas(avena, leche, mantequilla, pasa)
                galleta_3 = galleta3.preparacion()
                inventario.append(galleta_3)
            except UnboundLocalError:
                print("al inicio error de los ingredientes")
                continue
            print("BIEN ya lo tenemos")
            print(inventario)
            print("puedes irte")
            break
        else:
            print("al inicio")
            continue

    else:
        print("al incio")
        continue