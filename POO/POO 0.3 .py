#Alex:dame un reto aver si lo logro
#maestro.IA:¡Esa es la actitud de un Senior! Vamos a ver si puedes construir un sistema que conecte todo: Seguridad (Aduana),
#Herencia, Listas y Ciberseguridad.Este reto se llama "La Bóveda de los 3 Filtros".
#📝 El Escenario:Vas a crear un sistema para una empresa que fabrica Chips de Memoria. El Hijo es el Guardia de Seguridad
#y el Padre es la Máquina Grabadora.🛠️ Las Especificaciones:Clase Padre: GrabadoraSu __init__ recibe: modelo y lista_datos.
#Tiene un método def grabar(self) que imprime: "Grabando en {modelo} los siguientes datos: {lista_datos}".Clase Hijo:

#Aduana (Hereda de Grabadora)Su __init__ recibe: modelo y lista_datos.FILTRO 1 (El Virus): Antes del super(),
#debe revisar si la palabra "virus" está en la lista_datos. Si está, lanza un raise 
#ValueError("🚨 AMENAZA DETECTADA").FILTRO 2 (El Espía): Si el modelo es igual a "Hacker", debe cambiarlo automáticamente a "DESCONOCIDO"
#antes de mandarlo al padre.FILTRO 3 (La Memoria): Si la lista_datos tiene más de 3 elementos,
#debe lanzar un print("⚠️ Memoria llena, solo se grabarán los primeros 3") y recortar la lista usando Slicing ([:3]) 
#antes de mandarla al padre.
class Grabadora:
    def __init__(self, modelo, lista_datos):
        # Configura el padre aquí
        self.modelo = modelo
        self.lista_datos = lista_datos
    def grabar(self):
        print(f"grabando en {self.modelo} los siguientes datos: {self.lista_datos}")


class Aduana(Grabadora):
    def __init__(self, modelo, lista_datos):
        if "virus" in lista_datos:
            raise ValueError("AMENZA detectada")
        # 2. Filtro de Hacker (Cambia el nombre)
        if modelo == "Hacker":
            modelo = "DESCONOCIDO"
        
        # 3. Filtro de Memoria (Recorta la lista si es > 3)
        if len(lista_datos) > 3:
            print("MEMORIA LLENA solo se grabaran los primeros 3")
            lista_datos = lista_datos[:3]
        # 4. ENVIAR AL PADRE CON SUPER()
        super().__init__(modelo, lista_datos)

# --- LA PRUEBA DE FUEGO ---
try:
    # Prueba 1: Un chip con virus (Debe explotar)
    chip1 = Aduana("Pro", ["fotos", "virus", "musica"])
    
    # Prueba 2: Un chip muy pesado y con nombre Hacker
    chip2 = Aduana("Hacker", ["doc1", "doc2", "doc3", "doc4", "doc5"])
    chip2.grabar() 
    # Debería decir: Grabando en DESCONOCIDO los datos: ['doc1', 'doc2', 'doc3']

except ValueError as e:
    print(e)