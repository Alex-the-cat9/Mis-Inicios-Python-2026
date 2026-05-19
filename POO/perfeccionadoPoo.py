class TV:
    def __init__(self, television, **kwargs):
        if "barato".lower() in television: raise ValueError("el barato se malogro mientras se entregaba")
        else:print("Acceptado")
        print("Television entregada ahora sigue ventilador")
        super().__init__(**kwargs)
        self.television=television
        print("TELEVISION PRENDIDA DISFRUTE")
class Ventilador:
    def __init__(self, ventilador, **kwargs):
        if "barato".lower() in ventilador: raise ValueError("el barato se malogro mientras se entregaba")
        else:print("ACEPTADO")
        super().__init__(**kwargs)
        print("ventilador entregado Gracias por su compra")
        self.ventilador=ventilador
        print("VENTILADOR PRENDIDO DISFRUTE")
class Entrega(TV,Ventilador):
    lista = ["barato", "media", "caro"]
    def __init__(self):
        print("Barato Media Caro")
        tv = input("Cual de estas TV Quiere usted: ").lower().strip()
        ventilador = input("Ahora que ventilador quiere barato media oh caro: ").lower().strip()
        if tv in self.lista and ventilador in self.lista:print("Perfecto")
        else: tv,ventilador = "media","media"
        print("Entregando....")
        super().__init__(television=tv, ventilador=ventilador)
        print("entregado con exicto")
try:usuario=Entrega()
except ValueError:print("Se malogro xd")
else:
    print(Entrega.mro())


        

