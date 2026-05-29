class Personaje:
    def __init__(self, poder):
        self.poder = poder

    # 🎭 El camuflaje para que el print nos dibuje el poder final
    def __str__(self):
        return f"⚔️ [GUERRERO FUSIONADO] Poder cuántico total: {self.poder}"

    # 🔌 El interruptor del signo más que mezcla los componentes
    def __add__(self, otro):
        # Aplicamos la fórmula exacta de tu captura
        formula = self.poder + otro.poder
        
        # Devolvemos un objeto nuevo ya fusionado con ese poder
        return Personaje(poder=formula)


# --- CENTRAL DE INYECCIÓN DE ALEX ---
if __name__ == "__main__":
    print("⚡ === INICIALIZANDO PANEL DE FUSIÓN CUÁNTICA ===")
    
    # Creamos a los dos guerreros base en la RAM
    goku = Personaje(poder=10)
    vegeta = Personaje(poder=20)
    
    # 🚀 El signo "+" intercepta a goku (self) y a vegeta (otro)
    # Promedio: (10 + 20) / 2 = 15 | Al cuadrado: 15 * 15 = 225
    gogeta = goku + vegeta
    
    # Imprime el clon mutado con su poder de 225
    print(gogeta)