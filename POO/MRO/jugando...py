class paquete:
    def __init__(self, contenido, **kwargs):
        super().__init__(**kwargs)
        self.contenido = contenido
class precio:
    def __init__(self, precio, **kwargs):
        super().__init__(**kwargs)
        self.precio = precio
class envio(paquete,precio):
    def __init__(self, contenido, precio, ip):
        super().__init__(contenido=contenido, precio=precio)
        self.ip = ip
    def exito(self):
        if len(self.contenido) and len(self.ip):
            print("SE envio con exicto a su casa")
        else:
            print("ERROR de comprar")
contenido = input("que decea comprar?: ")
if len(contenido) < 2:contenido="cartitas"
ip = input("recuerde que todos nuestros productos estan 10$ diga su dirrecion: ").strip()
if len(ip) < 5:ip="NO definido"
user = envio(contenido, 10, ip)
user.exito()
#Alex:antes de ver el resultado del mro quiero predecir que va salir segun mis ojos primero envio luego paquete luego precio luego object
print(envio.mro())