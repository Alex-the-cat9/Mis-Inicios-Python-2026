#📋 Las Especificaciones del DesafíoDebes escribir un script en Python que cumpla exactamente estas 4 reglas lógicas:Clase Padre 1 
# (Guerrero): Su constructor debe recibir y guardar vida y espada (fuerza de ataque física). Debe tener un método 
# llamado atacar_fisico(self) que imprima el daño infligido.Clase Padre 2 (Hacker): Su constructor debe recibir y guardar ram_ataque 
# (fuerza de hackeo en GB) y virus_name. Debe tener un método llamado inyectar_malware(self) que imprima el nombre del virus siendo 
# ejecutado.Clase Hija Combinada (HackerGuerrero): Debe heredar de Guerrero y de Hacker en paralelo [INDEX_31]. Su constructor __init__
#  no recibirá parámetros fijos; en su lugar, debe pedirle los datos al usuario usando input().strip() (nombre del virus, vida, etc.)
#  y mandárselos a los constructores de sus padres usando el llamado explícito con el punto (Guerrero.__init__(self, ...)
#  y Hacker.__init__(self, ...)) [INDEX_34, INDEX_37].Polimorfismo de Reporte: El hijo supremo debe tener un método presentarse(self)
#  que use el polimorfismo para imprimir todas las variables combinadas de ambas herencias en un solo bloque estético de la terminal
#  [INDEX_34].🛠️ Tu Plantilla de Inicio (Completa los cables sueltos)Copia este bloque en tu VS Code y rellena las líneas marcadas
#  con ??? para que el script funcione sin letras rojas en la terminal:pythonclass Guerrero:
class Guerrero:
    def __init__(self, vida, espada):
        self.vida = vida
        self.espada = espada
    def atacar_fisico(self):
        print(f"⚔️ [ATAQUE] ¡Corte de espada letal inflige {self.espada} de daño!")

class Hacker:
    def __init__(self, ram_ataque, virus_name):
        self.ram_ataque = ram_ataque
        self.virus_name = virus_name
    def inyectar_malware(self):
        print(f"☣️ [EXPLOIT] Inyectando '{self.virus_name}' consumiendo {self.ram_ataque}GB de RAM...")

# 🧬 LA HERENCIA MÚLTIPLE: Agrega aquí los dos padres en el paréntesis
class HackerGuerrero(Guerrero ,Hacker):
    def __init__(self):
        print("💻 --- CREACIÓN DINÁMICA DEL HACKER GUERRERO ---")
        # 📥 Captura los datos desde el teclado
        vida = int(input("Digame la vida del personaje: "))
        fuerza = int(input("Digame la fuerza de la espada: "))
        ram = int(input("Digame los GB de RAM para hackear: "))
        virus = input("Digame el nombre de su virus señuelo: ").strip()

        # 🔌 CONECTA LOS CABLES: Envía los datos capturados a cada Padre usando el punto y el self
        Guerrero.__init__(self,vida, fuerza)
        Hacker.__init__(self,ram,virus)
    def presentarse(self):
        print("\n👑 === REPORTE DEL PERSONAJE SUPREMO ===")
        # Utiliza los casilleros configurados por los padres para mostrar el estado completo
        print(f"❤️ Vida: {self.vida} | 🗡️ Daño Físico: {self.espada}")
        print(f"🧠 Capacidad RAM: {self.ram_ataque}GB | 🦠 Carga Útil: {self.virus_name}")
try:
  Hacke = HackerGuerrero()
  Hacke.atacar_fisico()
  Hacke.inyectar_malware()
  Hacke.presentarse()
except ValueError:
    print("MAL")
