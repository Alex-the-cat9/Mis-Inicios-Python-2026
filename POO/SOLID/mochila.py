from modelo import Personaje
Personajes = {}
Personajes_fusionados = {}
def agregar_guerrero(nombre, poder):
    clon = Personaje(nombre, poder)
    Personajes[clon.nombre] = clon
def procesar_fusion(numero1, numero2):
    if len(Personajes) >= 2:
         guerrero1 = Personajes[numero1]
         guerrero2 = Personajes[numero2]
         fusion = guerrero1 + guerrero2
         del Personajes[numero1]
         del Personajes[numero2]
         Personajes_fusionados[fusion.nombre] = fusion
         return fusion
    else:
         return "mochila vacia"