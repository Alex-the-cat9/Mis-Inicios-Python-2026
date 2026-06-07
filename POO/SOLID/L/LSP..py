import abc

# 🏛️ 1. EL PADRE ABSTRACTO (El plano de hierro intocable - CERRADO)
class ArmaduraBase(abc.ABC):
    @abc.abstractmethod
    def activar_escudo(self, energia_inyectada):
        """El contrato exige estrictamente: self y UN número entero"""
        pass

# 🧬 2. HIJA 1: LA ARMADURA TOYOTA (Cumple la L)
class ArmaduraComun(ArmaduraBase):
    def __init__(self):
        self.defensa = 50

    def activar_escudo(self, energia_inyectada):
        # Hace su propia lógica interna limpia
        self.defensa += energia_inyectada
        return f"🛡️ Escudo común inflado a {self.defensa} de resistencia."

# 🧬 3. HIJA 2: LA ARMADURA BUNKER (¡Sustitución de Liskov perfecta!)
class ArmaduraBunkerMilitar(ArmaduraBase):
    def __init__(self):
        self.defensa = 500
        # 🔑 El secreto senior: El código de seguridad nace OCULTO en el constructor,
        # protegiendo la S y sin deformar el enchufe del método de acción.
        self._codigo_bunker = "1234" 

    def activar_escudo(self, energia_inyectada):
        # 🟢 CUMPLIENDO LA L: Recibe exactamente el mismo parámetro que el padre.
        # Puede suplantarlo en frío porque respeta la aduana de la firma.
        if self._codigo_bunker == "1234":
            self.defensa += (energia_inyectada * 2) # Tiene superpoder de absorción
            return f"🔥 ¡SUPER ESCUDO MILITAR ACTIVADO! Resistencia letal: {self.defensa}"


# 🛰️ 4. TU INTERFAZ INTERACTIVA (main.py - CERRADO A MODIFICACIONES)
if __name__ == "__main__":
    print("🛰️ === INICIALIZANDO ADUANA LISKOV ===")
    
    # Creamos un casillero de inventario con las dos armaduras mezcladas
    inventario_armaduras = [ArmaduraComun(), ArmaduraBunkerMilitar()]
    
    # 🔌 LA PRUEBA REINA: Recorremos las armaduras en un bucle 'for'
    for armadura in inventario_armaduras:
        # El programa principal le mete corriente a ciegas usando UN SOLO número (50).
        # La ArmaduraBunker suplanta al padre de forma transparente.
        # No hay 'if armadura == bunker', no hay 'TypeError', no hay letras rojas.
        reporte_ram = armadura.activar_escudo(50)
        
        print(reporte_ram)
#Alex:en ese entonces creo que ya entendi:la S que sus nombres no esten de por gusto que cumplan lo que dicen la O
#no puedes tocar a la clase padre pero si puedes crear tus clases hijas L todas las clases hijas deven tener un
#objetivo pero pueden cumplirlo de manera diferente