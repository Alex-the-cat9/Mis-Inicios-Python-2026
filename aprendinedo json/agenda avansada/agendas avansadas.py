import json
#Alex:estuve probando json por mucho tiempo le tenia miedo a la "w" porque borraba todo mi progreso
#Alex:pero mi maestro me explico que no lo hacia el dump hacia que no lo borrara por completo sin embargo
#Alex:si no le doy contenido a mi diccionario agenda la "w" pondra ese diccionario vacio por eso me dijo que siempre es mejor
#Alex:poner un try para cargar los archivos y un except para crearlo si no existen
try:
    with open("probar.json", "r") as f:
        agenda = json.load(f)
except FileNotFoundError:
    agenda = {}
    with open("probar.json", "w", encoding="utf-8") as f:
        json.dump(agenda, f, indent=4,ensure_ascii=False)
try:
    with open("papelera.json", "r") as f:
        papelera = json.load(f)
except FileNotFoundError:
    papelera = {}
    with open("papelera.json", "w", encoding="utf-8") as f:
        json.dump(papelera, f, indent=4, ensure_ascii=False)
def agregar_agenda(agenda):
    cedula = input("ponga la cedula: ")
    nombre = input("ponga su contacto: ")
    try:
      numero = int(input("ponga su numero: "))
    except ValueError:
        print("no letras cancelando agregar cedula..")
        return agenda
    agenda[cedula] = {"nombre":nombre, "numero":numero}
    print("agregado con exito")
    punto_de_guardado()
    return agenda
def punto_de_guardado():
    with open("probar.json", "w", encoding="utf-8") as f:
        json.dump(agenda, f, indent=4, ensure_ascii=False)
    with open("papelera.json", "w", encoding="utf-8") as f:
        json.dump(papelera, f, indent=4, ensure_ascii=False)
def eliminar_contacto(agenda):
    for e,i in agenda.items():
        print(f"cedula:{e} nombre:{i["nombre"]}")
    eliminar = input("que cedula decea eliminar?: ").lower()
    if eliminar in agenda:
        seguro = input("deseas eliminarlo de forma permanente? [si] [no]: ").lower()
        if seguro == "si":
            del agenda[eliminar]
            print(f"se a borrado de forma permanente:{eliminar}")
            punto_de_guardado()
        elif seguro == "no":
            papelera[eliminar] = agenda[eliminar]
            del agenda[eliminar]
            print(f"el antiguo archivo:{eliminar} se movio a la papelera y se borro de agenda")
            punto_de_guardado()
        else:
            print("opcion no valida")
    else:
        print("no se encuentra en la agenda")
def ver_o_mostrar(mostrar):
    for e,i in mostrar.items():
        print(f"cedula:{e} nombre:{i["nombre"]} numero:{i["numero"]}")
def buscador(buscador):
    buscar = input("ingrese la cedula oh el nombre del contacto para buscarlo: ").lower()
    encontrado = False
    if buscar in buscador:
        datos = buscador[buscar]
        print(f"encontrado por cedula nombre:{datos["nombre"]} telefono:{datos["numero"]}")
        encontrado = True
    else:
        for cedula,dato in buscador.items():
            if dato["nombre"].lower() == buscar:
                print(f"encontrado por nombre la cedula es:{cedula} nombre:{dato["nombre"]} numero:{dato["numero"]}")
                encontrado = True
                break
    if not encontrado:
        print("no encontrado ni con nombre ni con cedula")         
def recuperar_o_eliminar(papelera):
    ver_o_mostrar(papelera)
    pregunta = input("desea [recuperar] oh [eliminar] [salir] de su papelera?: ").lower()
    if pregunta == "salir":
        print("saliendo...")
        return
    elif pregunta == "eliminar":
        ver_o_mostrar(papelera)
        eliminar = input("que cedula decea eliminar: ")
        if eliminar in papelera:
            del papelera[eliminar]
            punto_de_guardado()
        else:
            print("opcion no valida")
    elif pregunta == "recuperar":
        ver_o_mostrar(papelera)
        recuperar = input("que cedula decea recuperar?: ")
        if recuperar in papelera:
            agenda[recuperar] = papelera[recuperar]
            del papelera[recuperar]
            punto_de_guardado()
        else:
            print("opcion no valida")
    else:
        print("opcion no valida saliendo..")
while True:
    preguntar = input("que decea hacer en su agenda [buscar] [papelera] [ver el contenido] [eliminar contacto] [agregar cedula] [salir]: ")
    if preguntar == "salir":
        print("saliendo...")
        break
    elif preguntar == "agregar cedula":
        agenda = agregar_agenda(agenda)
    elif preguntar == "eliminar contacto":
        eliminar_contacto(agenda)
    elif preguntar == "buscar":
        preguntar2 = input("desea buscar el contacto de la [papelera] oh de la [agenda]?: ").lower()
        if preguntar2  == "papelera":
            buscador(papelera)
        elif preguntar2 == "agenda":
            buscador(agenda)
        else:
            print("opcion no valida")
    elif preguntar == "ver el contenido":
        preguntar3 = input("que decea ver su [papelera] oh su [agenda]?: ").lower()
        if preguntar3 == "agenda":
            ver_o_mostrar(agenda)
        elif preguntar3 == "papelera":
            ver_o_mostrar(papelera)
        else:
            print("no exite esa opcion")
    elif preguntar == "papelera":
        recuperar_o_eliminar(papelera)
    else:
        print("esa opcion no existe")
