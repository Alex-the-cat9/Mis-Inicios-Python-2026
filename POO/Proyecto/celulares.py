import json
try:
    with open("celulares.json", "r")as f:celulares = json.load(f)
except FileNotFoundError:
    celulares = {"DINERO":0, "vendidos":[]}
    with open("celulares.json", "w", encoding="utf-8")as f:json.dump(celulares, f, indent=4, ensure_ascii=False)
def punto_de_guardado():
    with open("celulares.json", "w", encoding="utf-8")as f:json.dump(celulares, f, indent=4, ensure_ascii=False)
class Celular:
    def __init__(self, pantalla, nucleo, memoria, **kwargs):
        super().__init__(**kwargs)
        self.pantalla,self.nucleo,self.memoria = pantalla, nucleo,memoria
class Camara:
    def __init__(self, camaraFrontal, camaraTrasera): self.camaraFrontal,self.camaraTrasera = camaraFrontal, camaraTrasera
class Creacion(Celular, Camara):
    def __init__(self):
     pantalla = input("dime la potencia de tu pantalla: ").strip()
     if len(pantalla) <= 0: pantalla = "BAJA"
     nucleo = input("dime su potencia en nucleo: ").strip()
     if len(nucleo) <= 0: nucleo = "MEDIA"
     memoria = input("dime la memoria del celular: ").strip()
     if len(memoria) <=0: memoria = "56G"
     camaraFrontal = input("dime que tan potente quieres la camara: ").strip()
     camaraTrasera = input("dime que tan potente quieres la camara trasera: ").strip()
     if len(camaraFrontal) <= 0: camaraFrontal = "MEDIA"
     if len(camaraTrasera) <= 0: camaraTrasera = "MEDIA"
     celulares["vendidos"].append({"PANTALLA":pantalla, "NUCLEO":nucleo, "MEMORIA":memoria, "CAMARAFRONTAL":camaraFrontal, "CAMARATRASERA":camaraTrasera})

     celulares["DINERO"] += 300
     super().__init__(pantalla=pantalla, nucleo=nucleo, memoria=memoria, camaraFrontal=camaraFrontal, camaraTrasera=camaraTrasera)
    def mostrar(self):
        print(f"TU CELULAR: ")
        print(f"PANTALLA:{self.pantalla}")
        print(f"NUCLEO:{self.nucleo}")
        print(f"MEMORIA:{self.memoria}")
        print(f"CAMARA FRONTAL:{self.camaraFrontal}")
        print(f"CAMARA TRASERA:{self.camaraTrasera}")
        print("gracia por su comprar")
while True:
    usuario = input("desea comprar un celular? [si] [no]: ").lower()
    if usuario == "si": celular1 = Creacion(); celular1.mostrar();punto_de_guardado()
    else:
        print("okay siguiente")
        break
