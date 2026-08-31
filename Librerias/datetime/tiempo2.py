from datetime import datetime
ahora = datetime.now()
texto = ahora.strftime("%d/%m/%Y a las %H:%M")
print(ahora)
print(texto) 
print(ahora.strftime("año:%Y mes:%m dia:%d"))
print("....")
print(f"la hora es {ahora:%H:%M}")