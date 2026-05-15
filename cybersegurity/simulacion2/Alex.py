#Alex deves creear un sistema en donde se guarde nuestro datos como cuenta bancaria
#empresa y cosas nuestros datos
import json
try:
    with open("empresa.json", "r") as f:
        empresa = json.load(f)
except FileNotFoundError:
    empresa = {
    "empleados":{},
    "cuenta_bancaria":90000
}
    with open("empresa.json", "w", encoding="utf-8") as f:
        json.dump(empresa, f, indent=4, ensure_ascii=False)
def punto_de_guardado():
    with open("empresa.json", "w", encoding="utf-8") as f:
        json.dump(empresa, f, indent=4, ensure_ascii=False)
class añadir:
    def __init__(self, nombre, trabajo):
        self.nombre = nombre
        self.trabajo = trabajo
        empresa["empleados"][nombre] = trabajo
        punto_de_guardado()
class empleado(añadir):
    def __init__(self):
        self.empleos = ["vigilante", "limpieza", "constructor software", "vigilar los datos"]
        usuario = input("su nombre: ")
        empleo = input("su empleo [limpieza] [constructor software] [vigilar los datos]: ").lower()
        if empleo in self.empleos:
            print("bienvenido")
            super().__init__(usuario, empleo)
        else:
            print("invalido")
while True:
    user = input("quiere entrar?: ").lower()
    if user == "si":
        trabajo = empleado()
    elif user == "ver":
        for nombre, empleo in empresa.items():
            print(F"{nombre}:{empleo}")
    else:
        print("siguiente")

        
