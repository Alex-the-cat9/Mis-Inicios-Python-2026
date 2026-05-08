class celular():
    def __init__(self, modelo, marca, codigo):
        self.modelo = modelo
        self.marca = marca
        self.codigo = codigo
    def llamar(self):
        print("estas haciendo una llamada desde tu:", {self.modelo})
    def cortar(self):
        print("cortaste la llamada desde tu:", {self.modelo})
celular1 = celular("sansung", "A24", "1999")
celular1.llamar()