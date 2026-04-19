import time
print("eres un hacker ya lo tienes todo para hackear este sistema ")
   
while True:
    sistema = ["codigos", "documentos", "cuentas_Bancarias"]
    if len(sistema) == 3:
       hackear = int(input("Ahora estas a un boton para hackear este sistema inutil solo di el numero 10 que es el codigo para hackear: "))
    def limpiador():
       if len(sistema) > 4:
          print("Todo en orden no ay nada sospechoso")
       else:
          if sistema.count("VIRUS") > 0:
             for i in sistema:
                if "VIRUS" in i:
                   sistema.remove("VIRUS")
    if hackear == 10:
      sistema.insert(0, "VIRUS")
      print("JAJAJA ya metiste el virus ahora si por fin tendremos las cuentas bancarias")
      print("ahora miremos si se metio el virus")
      limpiador()
      time.sleep(3)
      for e in sistema:
         print(e)
      print("QUE no se metio el virus porque?")
      time.sleep(3)
      print("Hacker descuidado soy YO Alex soy el protector de este sistema mejor sera que te vayes por siempre oh tendre que llamar a la policia cybernetica")
      time.sleep(5)
      print("y por cierto sobre tu programa lamentablemente nunca va funcionar porque tenemos una funcion de limpieza que a cada segundo se usa solo si ay mas de 3 cosas en el sistema")
      time.sleep(5)
      print("ahora vete oh tendre que atacarte tambien hacker")
      if len(sistema) == 3:
         break
      else:
         limpiador()
    else:
       print("que estas haciendo cumple tu misiom") 
