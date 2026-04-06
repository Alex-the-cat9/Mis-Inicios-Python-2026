edad = []
rechazados = 0
aceptados = 0
nombres_de_rechazados = []
nombres_de_aceptados = []
edad_de_rechazados = []
edad_de_aceptados = []
def registro_rechazados():
    for nombres in (nombres_de_rechazados):
        print(f"nombre:{nombres} su edad:{edad_de_rechazados}")
def registro_aceptados():
    for nombres in (nombres_de_aceptados):
        print(f"nombre:{nombres} su edad:{edad_de_aceptados}")


while True:
    nombre = str(input("tu nombre porfavor: "))
    if nombre == "jefe":
        print("bienvenido jefe")
        break
    edad = int(input("que edad tienes?: "))
    if edad >= 18:
        print("puedes pasar")
        aceptados = aceptados +1
        nombres_de_aceptados.append(nombre)
        edad_de_aceptados.append(edad)

    else:
        print("no puedes pasar")
        rechazados = rechazados + 1
        nombres_de_rechazados.append(nombre)
        edad_de_rechazados.append(edad)
        
print("jefe estos son la lista de los rechazados:")
registro_rechazados()
print(f"total:{rechazados}")
print("--------------------")
print("jefe ahora este es el registro de los aceptados")
registro_aceptados()
print(f"total:{aceptados}")
print("--------------------")
print("eso fue todo jefe me retiro")