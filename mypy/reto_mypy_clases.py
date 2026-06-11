#El Reto: El Gestor de Suscripciones (Clases)Debes diseñar un sistema básico
#para gestionar clientes de una plataforma de streaming utilizando clases y asegurando que todos los
#atributos y métodos estén perfectamente tipados.
#Las Reglas del Negocio:Crea una clase llamada Usuario.El constructor (__init__) debe recibir y configurar tres atributos:nombre
#(cadena de texto)plan (cadena de texto, por ejemplo: "Básico" o "Premium")precio_base (número decimal / float)
#Agrega un método llamado calcular_total. Este método debe:Recibir un parámetro opcional llamado descuento
#(un float que por defecto sea 0.0).Aplicar el descuento al precio_base usando el operador -= y devolver el precio final
# como un float.Agrega un método llamado cambiar_plan. Este método debe:Recibir el nombre del nuevo_plan (str) y el 
#nuevo_precio (float).Actualizar los atributos correspondientes del usuario. Este método no debe devolver nada (None).
class Usuario:
    def __init__(self,nombre:str, plan:str, precio_base:float):
        self.nombre = nombre
        self.plan = plan
        self.precio_base = precio_base
    def calcula_total(self, descuento:float) -> float:
        self.precio_base -= descuento
        return self.precio_base
    def cambiar_plan(self,nuevo_plan:str) -> None:
        if nuevo_plan.lower() == "basico":
            self.precio_base = 50
        else:
            self.precio_base = 100
nombre = input("diga su nombre: ")
plan = input("diga su plan tenemos 2 [vip] [base]: ").lower()
if plan == "vip":
    print("muy buena decicion el vip esta 100")
    precio = 100
else:
    print("el basico es basico pero te ahorraras dinero")
    precio = 50
user1 = Usuario(nombre, plan, precio)
print("losiento no tiene descuentos")
user = input("le gustaria cambiar de plan? [si] o [no]: ").lower()
if user == "si":
    if user1.plan == "vip":
        user1.plan = "basico"
        user1.precio_base = 50
    else:
        user1.plan = "vip"
        user1.precio_base = 100
else:
    print("esta biem")
    
