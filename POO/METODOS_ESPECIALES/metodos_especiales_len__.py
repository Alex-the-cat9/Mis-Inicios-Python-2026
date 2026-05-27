class DetectarVirus:
    def __init__(self):
        self._Virus_detectados = []
        self._Virus_detectados.append("malware")
    def __len__(self):
        return len(self._Virus_detectados)
anti_Virus = DetectarVirus()
aguila = len(anti_Virus)
if aguila == 0:
    print("No ay virus")
if anti_Virus._Virus_detectados:
    print("ALERTA VIRUS DETECTADO")