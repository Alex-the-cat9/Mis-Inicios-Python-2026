class padre:
    def __init__(self,celular, **kwargs):
        super().__init__(**kwargs)
        self.celular = celular
class prueba:
    def __init__(self,cargador, **kwargs):
        super().__init__(**kwargs)
        self.cargador = cargador
class enchufe:
    def __init__(self, enchuf, **kwargs):
        super().__init__(**kwargs)
        self.enchuf = enchuf
class pantalla:
    def __init__(self, pantalla, **kwargs):
        super().__init__(**kwargs)
        self.pantalla = pantalla
class celular(padre,prueba,enchufe,pantalla):
    def __init__(self):
        celu = input("que celular deceas: ")
        if len(celu) <= 0:
            celu = "androi"
        carga = input("dime tu cargador: ")
        if len(carga) <= 0:
            carga = "cargador_androi"
        enchu = input("dime tu enchufe: ")
        if len(enchu) <= 0:
            enchu = "enchufe_barato"
        panta = input("dime tu pantalla: ")
        if len(panta) <= 0:
            panta = "pantalla_xd"
        super().__init__(celular=celu, cargador=carga, enchuf=enchu, pantalla=panta)
    def mostrar(self):
        print(f"celular:{self.celular}")
        print(f"cargador:{self.cargador}")
        print(f"enchufe:{self.enchuf}")
        print(f"pantalla:{self.pantalla}")
celular1 = celular()
celular1.mostrar()
