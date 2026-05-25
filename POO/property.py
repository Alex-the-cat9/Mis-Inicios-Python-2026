class ServidorIA:
    def __init__(self, nucleos_iniciales):
        self.__nucleos = nucleos_iniciales
    @property
    def nucleos(self):
        print("[GETTER] El Águila vuela en secreto y extrae el dato confidencial...")
        return self.__nucleos
    @nucleos.setter
    def nucleos(self, nuevo_valor):
        if nuevo_valor < 0:
            print("NO NUMEROS INVALIDOS")
            raise ValueError
        print("SETTERS")
        self.__nucleos = nuevo_valor


print("🛰️  === INICIALIZANDO NÚCLEO CUÁNTICO ===")
servidor = ServidorIA(1000)
aguila = servidor.nucleos
print(f" Núcleos verificados en el monitor: {aguila}")
try:
 servidor.nucleos = -999
 aguila_poderosa = servidor.nucleos
 print(aguila_poderosa)
except ValueError:
    print("NO numeros invalidos")