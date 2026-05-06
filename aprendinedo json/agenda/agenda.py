import json
agenda = {

}
def agregar_cedula(agenda):
    while True:
      try:
        cedula = input("ingrese su cedula: ")
        contacto = input("ingrese el nombre: ")
        numero = int(input("ingrese su numero: "))
        edad = int(input("ingrese su edad"))
      except ValueError:
         print("porfavor deve ser un numero")
         continue
      else:
         agenda[cedula] = {"contacto":contacto, "numero":numero, "edad":edad}
         with open("mi agenda.json", "w", encoding="utf-8") as f:
            json.dump(agenda, f, indent=4, ensure_ascii=False)
         break
    return agenda
def mostrar_agenda(agenda):
   
   for cedula,dato in agenda.items():
      print(f"su cedula es:{cedula} su contacto:{dato["contacto"]} su numero:{dato["numero"]} su edad: {dato["edad"]}")
while True:
    opinion = input("ingrese [agregar] si quiere agregar oh [mostrar] si quiere ver su agenda y [salir] para slair: ").lower()
    if opinion == "agregar":
      agenda = agregar_cedula(agenda)
    elif opinion == "salir":
      break
    elif opinion == "mostrar":
      mostrar_agenda(agenda)
    else:
       print("opcion no valida")

      