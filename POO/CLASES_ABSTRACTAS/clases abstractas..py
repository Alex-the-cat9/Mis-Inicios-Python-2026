from abc import ABC, abstractmethod

# =====================================================================
# 1. EL PLANO FANTASMA (La Clase Abstracta)
# =====================================================================
class PlanoBaseDroide(ABC):
    """
    Este es el supervisor del multiverso. Ningún Junior puede crear un 
    objeto directo de aquí. Su única misión es imponer la ley de nombres.
    """
    def __init__(self, numero_serie):
        # Todos los droides heredan este casillero de fábrica
        self.numero_serie = numero_serie

    # 🚨 LA LEY SUPREMA: Obligo a todo el multiverso a programar este método
    @abstractmethod
    def ejecutar_ataque(self):
        pass


# =====================================================================
# 2. LAS CLASES REALES (Hijos obligados a cumplir el contrato)
# =====================================================================
class DroideFuego(PlanoBaseDroide):
    def __init__(self, numero_serie, temperatura):
        # Despertamos al constructor padre para que guarde el número de serie
        super().__init__(numero_serie)
        self.temperatura = temperatura

    # ✅ Cumple el contrato: Usa exactamente el nombre obligatorio
    def ejecutar_ataque(self):
        print(f"🔥 [SERIE {self.numero_serie}] Lanzando ráfaga de fuego a {self.temperatura}°C.")


class DroideLaser(PlanoBaseDroide):
    def __init__(self, numero_serie, potencia_voltios):
        super().__init__(numero_serie)
        self.potencia = potencia_voltios

    # ✅ Cumple el contrato: Mismo interruptor, diferente circuito interno
    def ejecutar_ataque(self):
        print(f"⚡ [SERIE {self.numero_serie}] Disparando láser cuántico de {self.potencia}V.")


# =====================================================================
# 3. EL PANEL DE PRUEBAS DE ALEX (La ejecución en la RAM)
# =====================================================================
if __name__ == "__main__":
    print("🤖 === INICIALIZANDO CENTRAL DE INFRAESTRUCTURA MÁXIMA ===")

    # 🟢 Los droides reales nacen perfectos porque obedecieron tus planos
    bot_rojo = DroideFuego(numero_serie="DF-99", temperatura=1500)
    bot_azul = DroideLaser(numero_serie="DL-44", potencia_voltios=8000)

    # 🚀 LA VICTORIA DE UN ARQUITECTO: El bucle polimórfico limpio
    ejercito = [bot_rojo, bot_azul]
    print(PlanoBaseDroide.mro())
    
    for droide in ejercito:
        # Corren con una fluidez molecular perfecta porque el plano base
        # garantizó que todas las etiquetas se llamen 'ejecutar_ataque'
        droide.ejecutar_ataque()