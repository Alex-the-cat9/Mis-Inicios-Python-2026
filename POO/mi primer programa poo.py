class alagar:
    def __init__(sef,nombre,carisma):
        sef.nombre = nombre
        sef.carisma = carisma
    def ser_alagado(sef, victima):
        print(f"{sef.nombre} le dice a {victima} buenos dias")
        print(f"{victima} le devuelve el gusto")
gatito1 = alagar("Alex", 2)
gatito1.ser_alagado("victor")