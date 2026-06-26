palabras_comunes = ["perro", "gato", "pollo", "gallina", "alex", "erizo", "aire", "alegre", "tristre", "vaca", "jirafa"]
simbolos_especiales = ["@", ".", "'", "¿", "|", "-", "_", "{", "!", "[", "]", "/"]
def IA_porcentaje_de_hackeo(token:str):
    razon = []
    porcentaje = 0
    if len(token) > 20:
        porcentaje -= 20
    elif len(token) <= 15:
        razon.append("el token tiene menos de 15 caracteres")
        porcentaje += 50
    for a in simbolos_especiales:
        if a in token:
            porcentaje -= 20
    for i in palabras_comunes:
        if i in token.lower():
            razon.append("el token tiene palabras comunes")
            porcentaje += 10
            break
    if token.islower():
        porcentaje += 20
        razon.append("todo el token esta en minusculas ")
    elif token.isupper():
        porcentaje += 20
        razon.append("todo el token esta en mayusculas")
    if porcentaje <= 0:
        return "Casi imposible de hackear", ["no ay razones cumple todo", "no ay razones cumple todo"]
    return porcentaje, razon
    