#🩻 Las Especificaciones del Desafío: El Escáner de Tokens Vas a crear una clase llamada BunkerTokens
#El sistema central necesita saber cuántas llaves de acceso tienes activas en los chips usando el comando nativo
#de Python len(), sin revelar las llaves reales .⚠️ Las 2 Únicas Reglas del Circuito:El Saco Oculto:
#En el constructor (__init__), inicializa una lista llamada self._tokens que contenga tres textos de llaves falsas
#(por ejemplo: ["T-100", "T-200", "T-300"]) .El Interceptor de Conteo (__len__): Programa el método especial def __len__(self):
#para que intercepte el comando len() de fábrica y regrese con un return la cantidad exacta de elementos que tiene tu lista
class BunkerTokens:
    def __init__(self):
        self.__tokens = ["T-100", "T-200", "T-200"]
    def __len__(self):
        return len(self.__tokens)
tokens = BunkerTokens()
aguila = len(tokens)
if aguila <= 0:
    print("NO ay tokens")
else:
    print("SI AY TOKENS")