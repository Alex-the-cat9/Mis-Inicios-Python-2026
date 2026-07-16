from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel
from secrets import token_hex
admin = token_hex(15)
with open("administracion.text", "w") as f:
    f.write(admin)
app = FastAPI(title="Api de Creacion de autos / simulador NO profesional", docs_url=f"/{admin}")
@app.get("/")
def bienvenida():
    return "bienvenido puede ir a 'creacion' para crear su auto\
        deve poner combustible(int) marca(str) velocidad(int) y clave(str de mas de 5 digitos) en formato JSON"
class estructura(BaseModel):
    combustible:int
    marca:str
    velocidad:int
    clave:str | int
class combustible:
    def __init__(self, combustible, **kwargs):
        super().__init__(**kwargs)
        self.combustible = combustible
class marca:
    def __init__(self, marca, **kwargs):
        super().__init__(**kwargs)
        self.marca = marca
class velocidad:
    def __init__(self, velocidad, **kwargs):
        super().__init__(**kwargs)
        self.velocidad_maxima = velocidad
class clave:
    def __init__(self, clave, **kwargs):
        super().__init__(**kwargs)
        self.__clave = clave
class auto(combustible, marca, velocidad, clave):
     def __init__(self, combustible, marca, velocidad, clave):
          super().__init__(combustible=combustible, marca=marca, velocidad=velocidad, clave=clave)
marcas = [
    "Alpina", "Apollo Automobile", "Artega", "Audi", "Bitter", "BMW", "Borgward", 
    "Brabus", "Gumpert", "Isdera", "Maybach", "Mercedes-Benz", "Opel", "Porsche", 
    "Ruf", "Smart", "Volkswagen",
    "Buick", "Cadillac", "Callaway", "Chevrolet", "Chrysler", "Czinger", "DeLorean", 
    "Dodge", "Faraday Future", "Fisker", "Ford", "GMC", "Hennessey", "Jeep", "Karma", 
    "Lincoln", "Local Motors", "Lucid Motors", "Panoz", "RAM", "Rivian", "Rossion", 
    "Saleen", "Scuderia Cameron Glickenhaus", "Shelby", "Tesla",
    "Acura", "Autozam", "Daihatsu", "Eunos", "Honda", "Infiniti", "Isuzu", "Lexus", 
    "Mazda", "Mitsubishi", "Mitsuoka", "Nissan", "Subaru", "Suzuki", "Tommykaira", 
    "Toyota",
    "Aito", "Arcfox", "Avatr", "BAIC", "Brilliance", "BYD", "Changan", "Chery", 
    "Deepal", "Denza", "Dongfeng", "Fang Cheng Bao", "Faw", "GAC Motor", "Geely", 
    "Great Wall", "Havall", "HiPhi", "Hongqi", "IM Motors", "JAC Motors", "Jaecoo", 
    "JiYue", "Leapmotor", "Lifan", "Lynk & Co", "Maxus", "MG", "NIO", "Omoda", 
    "Voyah", "Wuling", "Xiaomi", "Xpeng", "Yangwang", "Zeekr", "Zotye",
    "Abarth", "Alfa Romeo", "Bengineering", "Dallara", "DR Automobiles", "Ferrari", 
    "FIAT", "Frangivento", "Iso Rivolta", "Lamborghini", "Lancia", "Maserati", 
    "Mazzanti", "Pagani", "Pininfarina",
    "Ariel", "Aston Martin", "BAC", "Bentley", "Bowler", "Caterham", "Ginetta", 
    "Gordon Murray Automotive", "Ineos Automotive", "Jaguar", "Land Rover", "Lister", 
    "Lotus", "McLaren", "MINI", "Morgan", "Noble", "Radical", "Rolls-Royce", "TVR", 
    "Zenos",
    "Aixam", "Alpine", "Bugatti", "Citroën", "Delage", "DS Automobiles", "Ligier", 
    "Microcar", "Peugeot", "Renault", "Venturi",
    "Genesis", "Hyundai", "KGM", "Kia", "Oullim Motors",
    "Koenigsegg", "Polestar", "SAAB", "Volvo",
    "CUPRA", "GTA Spano", "Hispano-Suiza", "Hurtan", "SEAT", "Tramontana",
    "Aurus", "Bollinger", "Dacia", "Donkervoort", "Gillet", "Holden", "KTM", "Lada", 
    "Laraki", "Mahindra", "Mastretta", "Perodua", "Proton", "Rimac", "Skoda", 
    "Tata Motors", "Troller", "Tushek", "VinFast", "VUHL", "W Motors", "Zenvo"
]
@app.post("/creacion", status_code=status.HTTP_201_CREATED)
def creacion(Base:estructura):
            if Base.velocidad >= 500:
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Velocidad demasiado rapido no se puede crear carro rechazado"
                )
            elif Base.marca in marcas:
                 raise HTTPException(
                      status_code=status.HTTP_400_BAD_REQUEST,
                      detail="carro rechazado por copyright te ayudamos a evitarte una demanda"
                 )
            elif Base.combustible >= 500:
                 raise HTTPException(
                      status_code=status.HTTP_400_BAD_REQUEST,
                      detail="el carro tiene un tanque enorme carro rechazado"
                 )
            elif type(Base.clave) == int and Base.clave < 5:
                 raise HTTPException(
                      status_code=status.HTTP_400_BAD_REQUEST,
                      detail="clave muy corta"
                 )
            elif type(Base.clave) == str and len(Base.clave) < 5:
                 raise HTTPException(
                      status_code=status.HTTP_400_BAD_REQUEST,
                      detail="clave muy corta"
                 )
            else:
                 nuevo = auto(combustible=Base.combustible, marca=Base.marca, velocidad=Base.velocidad, clave=Base.clave)
                 return {
                      "resultado":"autocreado",
                      "combustible":nuevo.combustible,
                      "marca":nuevo.marca,
                      "velocidad":nuevo.velocidad_maxima,
                      "clave":Base.clave
                 }
